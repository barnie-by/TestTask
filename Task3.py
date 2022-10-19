# import bs4
# import json
# from bs4 import BeautifulSoup
# import requests
#
# import re
# from re import sub
# from decimal import Decimal
# import io
# from datetime import datetime
# import pandas as pd
#
# url = 'https://naturasiberica.ru/our-shops/'
# url_base = 'https://naturasiberica.ru'
# html_text = requests.get(url).text
# soup = BeautifulSoup(html_text, 'lxml')
#
# # all_info = soup.find_all('a', class_='card-list__link')
# # link = all_info[0].find('href')
# all_info = soup.select('.card-list a')
# one_shop_href = all_info[0]['href']
# full_shop_url = url_base + one_shop_href
#
# page_url = requests.get(full_shop_url, timeout=10)
# soup_page_data = BeautifulSoup(page_url.text, 'html.parser')
#
# x = soup.find('div', class_='original-shops__settings-block').find('div', class_='original-shops__info')
# working_hours = soup.find('div', class_='shop-schedule original-shops__schedule').text
# # a = requests.get(x,)
# res = requests.post('https://naturasiberica.ru/local/php_interface/ajax/getShopsData.php', headers={
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
#     "X-Requested-With": "XMLHttpRequest"
# }, data={'type': 'all'})
# print(res.json())
# print(full_shop_url)
# print(x)
# print(working_hours)


# import os
# import json
# import requests
#
# if not os.path.exists('data.json'):
#     res = requests.post('https://naturasiberica.ru/local/php_interface/ajax/getShopsData.php', headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
#         "X-Requested-With": "XMLHttpRequest"
#     }, data={'type': 'all'})
#
#     with open('data.json', 'w', encoding='utf-8') as fp:
#         json.dump(res.json().get('original'), fp, indent=4, ensure_ascii=False)
#
# with open('data.json', 'r', encoding='utf-8') as fp:
#     data = json.load(fp)
#
# for item in data:
#     if item.get('phone'):
#         print({'city': item.get('city'),
#                'address': item.get('address'), 'phone_number': item.get('phone'),
#                'working_hours': item.get('schedule')})
#
#         new_data = {'city': item.get('city'),
#                     'address': item.get('address'), 'phone_number': item.get('phone'),
#                     'working_hours': item.get('schedule')}
#
#         with open('task_3_results.json', 'a', encoding='utf-8') as file:
#             json.dump(new_data, file, indent=1, ensure_ascii=False)



import os
import json
import requests


def format_item(item):
    return {
        'city': item.get('city'),
        'address': item.get('address').replace('&quot;', '"'),
        'phone_number': item.get('phone'),
        'working_hours': item.get('schedule'),
    }


if not os.path.exists('task_3_results.json'):
    res = requests.post('https://naturasiberica.ru/local/php_interface/ajax/getShopsData.php', headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }, data={'type': 'all'})

    with open('task_3_results.json', 'w', encoding='utf-8') as fp:
        json.dump([format_item(item) for item in res.json().get('original')], fp, indent=4, ensure_ascii=False)

with open('task_3_results.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)


for item in data:
    print(item)