import json
from bs4 import BeautifulSoup
import requests

# url сайта, к которому далее будет прибавляться id магазина
site_name = 'https://som1.ru'

# доступ к сайту только так вышло получить
res = requests.get('https://som1.ru/shops/', headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
})

# залоговки поместил в переменную, чтобы потом не писать их
zagolovki = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
ID_CITY = [3215, 3325, 2015, 2014, 3349, 3441, 3648, 2011, 3392, 2012, 2010, 3630, 2013, 3384, 3605, 3629, 3633, 3581,
           3632, 3645, 3667, 3653]

# тут получаю всю страницу где CITY_ID
data_list = []
for id in ID_CITY:
    data = requests.post('https://som1.ru/shops/', data={'CITY_ID': id}, headers=zagolovki)
    soup = BeautifulSoup(data.text, 'html.parser')

    # получаю ссылку на страницу, которая лежит в кнопке
    button_url = soup.select_one('.shops-button a').get('href')

    # прибавляем полученную ссылку к начальному адресу страницы, чтобы получить полную ссылку страницы с информацией магазина
    url = site_name + button_url

    # получение страницы магазина
    page_data = requests.get(url, headers=zagolovki)
    soup_page_data = BeautifulSoup(page_data.text, 'html.parser')
    info = soup_page_data.select('.shop-info-table tr')

    # получение данных о магазине
    name = soup_page_data.find('h1').text
    address = info[0].find('div').find_next('td').find_next('td').text
    phone_number = info[1].find('div').find_next('td').find_next('td').text
    working_hours = info[2].find('div').find_next('td').find_next('td').text

    new_data = {'name': name, 'address': address, 'phone_number': phone_number, 'working_hours': working_hours}
    data_list.append(new_data)

    # вывод данных в консоль
    print({'name': name, 'address': address, 'phone_number': phone_number, 'working_hours': working_hours})

# запись данных в json файл
with open('task_2_results.json', 'a', encoding='utf-8') as file:
    json.dump(data_list, file, indent=1, ensure_ascii=False)
