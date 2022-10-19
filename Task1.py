import json
from bs4 import BeautifulSoup
import requests

url = 'https://oriencoop.cl/sucursales/79'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
# решил таким образом перебрать страницы, поскольку их номера были на сайте
page = [79, 127, 165, 167, 170, 173, 180, 182, 184, 187, 188, 194, 196, 208, 219, 231, 267, 312]
datas_list = []
for el in page:
    url = 'https://oriencoop.cl/sucursales/' + str(el)
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

    new_data = {'name': name, 'address': address.string, 'phone': phone, 'working_hours': work_time_1 + work_time_2}

    datas_list.append(new_data)

    # вывод в консоль данных
    print({'name': name, 'address': address.string, 'phone': phone, 'working_hours': work_time_1 + work_time_2})

# запись данных в json файл
with open('task_1_results.json', 'a', encoding='utf-8') as file:
    json.dump(datas_list, file, indent=1, ensure_ascii=False)
