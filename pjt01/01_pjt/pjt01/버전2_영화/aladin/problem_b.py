import json
from pprint import pprint


def book_info(book, categories):
    new_data = {
        'author': book.get('author'),
        'categoryName': book.get('categoryId'),
        'cover': book.get('cover'),
        'description': book.get('description'),
        'id': book.get('id'),
        'priceSales': book.get('priceSales'),
        'title': book.get('title')
    }
    new_list = []
    for i in range (len(categories_list)):
        if book.get('categoryId')[0] == (categories_list[i]['id']):
            new_list.append(categories_list[i]['name'])
        elif book.get('categoryId')[1] == (categories_list[i]['id']):
            new_list.append(categories_list[i]['name'])
        else:
            continue

    new_data.update(categoryName = new_list)

    return new_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))


         
         