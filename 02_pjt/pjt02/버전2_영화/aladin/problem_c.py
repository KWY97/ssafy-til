import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
    'ttbkey': 'ttbskajtwlkt1146001',
    'Query': '파울로 코엘료',
    'QueryType': 'Author',
    'MaxResults': 20,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
}

response = requests.get(URL, params=params).json()
info_list = response.get('item')

def get_bestseller_books():
    new_dict = dict()
    ans_list = []

    for i in info_list:
        for j in info_list:
            key_1 = (j['title'])
            value_1 = (j['salesPoint'])
            new_dict.setdefault(key_1, value_1)
        sorted_dict = sorted(new_dict.items(), key = lambda item:item[1], reverse = True)

    sorted_tuple = sorted_dict[:5]

    for k in range(len(sorted_tuple)):
        ans_dict = dict()
        ans_dict['제목'] = sorted_tuple[k][0]
        ans_dict['판매지수'] = sorted_tuple[k][1]
        ans_list.append(ans_dict)

    return ans_list

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_bestseller_books())
