from requests import get, post
from math import sqrt
import pytest
import json


class TestApi():
    test_url = 'http://api.mathjs.org/v1/'
    headers = {
        'User-Agent': 'Python Learning Requests',
    }
    def sqrt_response(self, value='', precision=''):
        payloads = {'expr': f'sqrt({value})','precision': f'{precision}'}
        response = get(self.test_url, headers=self.headers, params=payloads)
        return response.text

    @pytest.mark.sqrt
    def test_sqrt_response(self):
        assert float(self.sqrt_response(value='48', precision='3')) == round(sqrt(48),2)
    
    @pytest.mark.sqrt_empty
    def test_sqrt_empty_response(self):
        assert self.sqrt_response() != ''
    
    def post_response(self, operation, value1, value2, precision=0):
        payloads = {'expr': f'{value1} {operation} {value2}', 'precision': precision}
        response = post(self.test_url, headers=self.headers, data=json.dumps(payloads)).text
        return response
    
    @pytest.mark.plus
    def test_plus_response(self):
        test_dict = json.loads(self.post_response('+', 1, 2))
        assert test_dict['result'] == str(3)
        assert test_dict['error'] == None
    
    @pytest.mark.multiple
    def test_multiple_response(self):
        test_dict = json.loads(self.post_response('*', 1, 2))
        assert test_dict['result'] == str(2)
        assert test_dict['error'] == None
    
    @pytest.mark.divide
    def test_divide_response(self):
        test_dict = json.loads(self.post_response('/', 1, 3, precision=3))
        assert test_dict['result'] == str(round(1/3, 3))
        assert test_dict['error'] == None
    
    @pytest.mark.subtract
    def test_subtract_response(self):
        test_dict = json.loads(self.post_response('-', 1, 3))
        assert test_dict['result'] == str(1-3)
        assert test_dict['error'] == None