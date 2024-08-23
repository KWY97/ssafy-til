# import requests
# from pprint import pprint



# def get_author_other_books(title):
#     if title == '*':
#         return None

#     params = {
#         'ttbkey': 'ttbskajtwlkt1146001',
#         'Query': title,
#         'QueryType': 'Title',
#         'MaxResults': 20,
#         'start': 1,
#         'SearchTarget': 'Book',
#         'output': 'js',
#         'Version': '20131101',
#     }

#     URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

#     response = requests.get(URL, params=params).json()
#     info_list = response.get('item')

#     author = info_list[0]['author']

#     first_author = author.split(',')[0]
#     first_author = first_author[::-1][6:][::-1]

#     params['Query'] = first_author
#     params['QueryType'] = 'Author'

#     response = requests.get(URL, params=params).json()
#     info_list_2 = response.get('item')

#     count = 0
    

#     while count != 5:
#         title_list = []
#         if info_list_2[count]['title'] != title:
#             title_list.append(info_list_2[count]['title'])
#             count += 1
#         else:
#             continue
    
#     result = {f'"{title}"의 저자 "{first_author}"의 다른 도서 목록': title_list}

#     return result

# # # 아래 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     pprint(get_author_other_books('베니스의 상인'), width=120)
#     pprint(get_author_other_books('죄와 벌'), width=120)
#     pprint(get_author_other_books('*'), width=120)

# # get_author_other_books('베니스의 상인')
# # get_author_other_books('죄와 벌')
# # get_author_other_books('*')


import requests

def get_author_other_books(title):
    if title == '*':
        return None

    params = {
        'ttbkey': 'ttbskajtwlkt1146001',
        'Query': title,
        'QueryType': 'Title',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    response = requests.get(URL, params=params).json()
    info_list = response.get('item')

    if not info_list:
        return None

    author = info_list[0]['author']
    first_author = author.split(',')[0]
    first_author = first_author[::-1][6:][::-1]

    params['Query'] = first_author
    params['QueryType'] = 'Author'

    response = requests.get(URL, params=params).json()
    info_list_2 = response.get('item')

    if not info_list_2:
        return None

    title_list = []
    for book in info_list_2:
        if book['title'] != title:
            title_list.append(book['title'])
        if len(title_list) == 5:
            break

    result = {f'"{title}"의 저자 "{first_author}"의 다른 도서 목록': title_list}
    return result

# # 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(get_author_other_books('베니스의 상인'))
    print(get_author_other_books('죄와 벌'))
    print(get_author_other_books('*'))