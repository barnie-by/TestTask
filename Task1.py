# import bs4
# from bs4 import BeautifulSoup
# import requests
#
# info_number = 79
#
# while True:
#     url = ('https://oriencoop.cl/sucursales/' + str(info_number))
#     html_text = requests.get(url).text
#     soup = BeautifulSoup(html_text, 'lxml')
#
#     if len(html_text):
#         # находим одно объявление
#         all_info = soup.find('div', class_='s-dato').find_all('p')
#
#         # внизу две строки находят адрес и потом вывожу адрес без тегов и лишнего
#         address_with_tags = soup.find('div', class_='s-dato').find_next('p')
#         address = address_with_tags.find('span')  # нужный адрес
#
#         name = soup.find('div', class_='s-dato').find_next('h3').text  # нужное имя
#         phone = all_info[1].find('span').text  # номер телефона
#         work_time_1 = all_info[2].find('span').find_next('span').text
#         work_time_2 = all_info[3].find('span').find_next('span').text
#
#         adres = soup.find_all('p', class_=False, id=False)
#
#         # print(name)
#         # print(address.string)
#         # print(phone)
#         # print(work_time_1)
#         # print(work_time_2)
#         try:
#             print({'name': name, 'address': address.string, 'phone': phone, 'working_hours': work_time_1 + work_time_2})
#
#         except Exception:
#             info_number += 1
#             continue


# print(all_info)
# print(address)
# print(adres)


# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get('https://oriencoop.cl/sucursales/127')
# soup = BeautifulSoup(r.content)
#
# data = soup.find('div', {'class': 's-dato'}).find_all('p')
#
# # print(data)
# print({'address': data[0].find('span').text, 'name': 'Oriencoop', 'phone': data[1].find('span').text})


# working code

import bs4
import json
from bs4 import BeautifulSoup
import requests

url = 'https://oriencoop.cl/sucursales/79'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
page = [79, 127, 165, 167, 170, 173, 180, 182, 184, 187, 188, 194, 196, 208, 219, 231, 267, 312]
data_list = []
for el in page:
    url = 'https://oriencoop.cl/sucursales/' + str(el)
    # print(url)

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    # находим одно объявление
    all_info = soup.find('div', class_='s-dato').find_all('p')

    # внизу две строки находят адрес и потом вывожу адрес без тегов и лишнего
    address_with_tags = soup.find('div', class_='s-dato').find_next('p')
    address = address_with_tags.find('span')  # нужный адрес
    name = soup.find('div', class_='s-dato').find_next('h3').text  # нужное имя
    phone = all_info[1].find('span').text  # номер телефона
    work_time_1 = all_info[2].find('span').find_next('span').text  # время работы
    work_time_2 = all_info[3].find('span').find_next('span').text

    # adres = soup.find_all('p', class_=False, id=False)

    # print(name)
    # print(address.string)
    # print(phone)
    # print(work_time_1)
    # print(work_time_2)

    # print({'name': name, 'address': address.string, 'phone': phone, 'working_hours': work_time_1 + work_time_2})
    new_data = {'name': name, 'address': address.string, 'phone': phone, 'working_hours': work_time_1 + work_time_2}

    data_list.append(new_data)
    # breakpoint()
    print(data_list)
    # def write(data, filename):
with open('task_1_results.json', 'a', encoding='utf-8') as file:
    json.dumps(data_list, indent=1, ensure_ascii=False)

    # write(new_data, 'task_1_results.json')
