import re
from os.path import dirname, join
from typing import Dict
def get_eid(source_file: str) -> Dict:
    current_dir = dirname(__file__)
    file_path = join(current_dir, f"./{source_file}")
    pattern = r'eid: .*'
    try:
        # Get two last lines with eid data
        with open(file_path, 'r') as file:
            eid_list = list(filter(lambda x: re.search(pattern, x), file.readlines()))[-2:]
        # Get list of lists of two last eid-lines in format 'key.value'
        pattern = r"\w{3}\.\d{1}"
        eid_list_data = list(map(lambda x: re.findall(pattern,x), eid_list))
        del eid_list
        # Create dicts
        eid_dict1 = {s[:3]: s[-1:] for s in eid_list_data[0]}
        eid_dict2 = {s[:3]: s[-1:] for s in eid_list_data[1]}
        del eid_list_data
        print(f'Prelast eid: {eid_dict1}')
        print(f'Last eid: {eid_dict2}')
        # Get all keys from 2 dicts
        all_keys = eid_dict1.keys() | eid_dict2.keys()
        compare_dict = {}
        # Create dict of differences
        for i in all_keys:
            if eid_dict1.get(i) != eid_dict2.get(i):
                if eid_dict2.get(i) is None:
                    compare_dict[i] = None
                else:
                    compare_dict[i] = eid_dict2[i]
        return compare_dict
    except FileNotFoundError:
        print('Your file is not found in current directory.')



if __name__ == '__main__':
    print(get_eid('for_test.log'))
