import json
from pprint import pprint


def books_info(books, categories):
    new_data = {
        'author': books[i]['author'],
        'categoryId': books.get('categoryId')
    }
#         'cover': books.get('cover'),
#         'description': books.get('description'),
#         'id': books.get('id'),
#         'priceSales': books.get('priceSales'),
#         'title': books.get('title')
#     }
#     new_list = []
#     for i in range (len(categories_list)):
#         if books.get('categoryId')[0] == (categories_list[i]['id']):
#             new_list.append(categories_list[i]['name'])
#         elif books.get('categoryId')[1] == (categories_list[i]['id']):
#             new_list.append(categories_list[i]['name'])
#         else:
#             continue

#     new_data.update(categoryId = new_list)

#     return new_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    # pprint(books_info(books, categories_list))





for i in range(len(books)):
    author = books[i]['author']
    categoryName = books[i]['categoryId']
    cover =  books[i]['cover']
    description = books[i]['description']
    id = books[i]['id']
    priceSales = books[i]['priceSales']
    title = books[i]['title']
