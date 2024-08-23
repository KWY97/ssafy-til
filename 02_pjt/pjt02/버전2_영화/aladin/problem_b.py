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

def get_best_review_books():
    high_rank_list = [info_list[i] for i in range(len(info_list)) if info_list[i]['customerReviewRank'] >= int(9)]
    
    return high_rank_list


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_best_review_books())
