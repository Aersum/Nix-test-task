import re
from os.path import dirname, join
from typing import Dict
def get_eid(source_file: str) -> Dict:
    current_dir = dirname(__file__)
    file_path = join(current_dir, f"./{source_file}")
    pattern = r'eid: .*'
    try:
        with open(file_path, 'r') as file:
            eid_list = list(filter(lambda x: re.search(pattern, x), file.readlines()))[-2:]
        pattern = r"\w{3}\.\d{1}"
        eid_list_data = list(map(lambda x: re.findall(pattern,x), eid_list))
        del eid_list
        eid_dict1 = {s[:3]: s[-1:] for s in eid_list_data[0]}
        eid_dict2 = {s[:3]: s[-1:] for s in eid_list_data[1]}
        del eid_list_data
        print(f'Prelast eid: {eid_dict1}')
        print(f'Last eid: {eid_dict2}')
        print(eid_dict1.keys()-eid_dict2.keys())
        print(eid_dict2.values())
    except FileNotFoundError:
        print('Your file is not found in current directory.')



if __name__ == '__main__':
    get_eid('for_test.log')
