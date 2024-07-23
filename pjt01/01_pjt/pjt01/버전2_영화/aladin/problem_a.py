import json
from pprint import pprint


def book_info(book):
    new_data = {
        'author': book.get('author'),
        'categoryId': book.get('categoryId'),
        'cover': book.get('cover'),
        'description': book.get('description'),
        'id': book.get('id'),
        'priceSales': book.get('priceSales'),
        'title': book.get('title')
    }

    return new_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json) # JSON 형식의 문자열을 파싱하여 python Dictionary로 변환
    # 파싱(parsing): 데이터를 의미 있는 구조로 분석하고 해석하는 과정

    pprint(book_info(book))

