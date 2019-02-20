from selenium import webdriver
from selenium.webdriver.support import ui
from hamcrest import assert_that, equal_to
import json
from page import Order
from cust_data import cust_data


class TestOrderForm:
    def page_is_loaded(self, driver):
        return driver.find_element_by_tag_name('body') is not None

    def setup(self):
        self.driver = webdriver.Chrome('../chrdrv/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://httpbin.org/forms/post"

    def test_is_equal_data(self):
        driver = self.driver
        driver.get(self.base_url)
        wait = ui.WebDriverWait(driver, 10)
        wait.until(self.page_is_loaded)
        order = Order(driver)
        order.CustomerName(cust_data['custname'])
        order.Telephone(cust_data['custtel'])
        order.EmailAddress(cust_data['custemail'])
        order.Comments(cust_data['comments'])
        order.DeliveryTime(cust_data['delivery'])
        order.PizzaSize(cust_data['size'])
        order.PizzaToppings(cust_data['topping'])
        order.SubmitOrder()
        response_form = json.loads(driver.find_element_by_tag_name('pre').text)['form']
        driver.close()
        for k, v in response_form.items():
            assert_that(cust_data[k], equal_to(v), k)
