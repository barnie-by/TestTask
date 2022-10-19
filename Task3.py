import os
import json
import requests


def format_item(item):
    return {
        'city': item.get('city'),
        'address': item.get('address'),
        'phone_number': item.get('phone'),
        'working_hours': item.get('schedule'),
    }


# Доступ к данным только так удалось получить, оказалось, что нужные данные лежат в файле, а не просто на странице
# и дальше уже работал с файлом, из него получал нужные данные и записал потом в новый json файл
if not os.path.exists('task_3_results.json'):
    res = requests.post('https://naturasiberica.ru/local/php_interface/ajax/getShopsData.php', headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }, data={'type': 'all'})

    # запись в json файл
    with open('task_3_results.json', 'w', encoding='utf-8') as fp:
        json.dump([format_item(item) for item in res.json().get('original')], fp, indent=4, ensure_ascii=False)

#  для вывода в консоль
with open('task_3_results.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)

for item in data:
    print(item)
