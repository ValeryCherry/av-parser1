# from colorama import Fore, Back, Style
# from colorama import init
#
# from datetime import datetime
# from bs4 import BeautifulSoup
# from fs.osfs import OSFS
# from lxml import html
# import pandas as pd
# import requests
# import random
# import shutil
# import time
# import csv
# import math
# import os
#
#
#
#
#
#
# init(autoreset=True)
# URL = 'https://av.by'
# today = datetime.today()
# print_today = f'{today:%H-%M-%S_%d-%m-%Y}'
#
#
# # ````функция получение количества объявлений и сохранение на диск```
# def alpha(link):
#     global n_title
#
#     req = requests.get(link)
#     file = open('result_data/temp.html', 'w', encoding='UTF8')
#     new_record = req.text
#     file.write(str(new_record))
#     file.close()
#     print(f'Информация о моделе {link} успешна сохранена\n')
#     time.sleep(random.randint(1, 3))
#
#     with open('result_data/temp.html', 'r', encoding='UTF8') as f:
#         contents = f.read()
#         soup = BeautifulSoup(contents, 'lxml')
#         listing_title = soup.find('h3', class_='listing__title').text
#         listing_title = listing_title.strip().split()
#         n_title = int(listing_title[1])
#         print(f'Найдено: {n_title} объявлений')
#
#     num_page = math.ceil(n_title / 25)
#
#     for page in range(1, num_page + 1):
#         page_name = 'result_' + str(page) + '.html'
#         req = requests.get(link)
#         file = open(f'result_data/{page_name}', 'w', encoding='UTF8')
#         new_record = req.text
#         file.write(str(new_record))
#         file.close()
#         print(f'Страница: {page_name} успешна сохранена\n')
#         time.sleep(random.randint(1, 10))
#
#
# # ````проверка наличия файлов в каталоге``````````````````````````````
# def control_files():
#     with OSFS("") as myfs:
#         work_dir = []
#         global cars
#         cars = []
#         for path in myfs.walk.dirs():
#             work_dir.append(path)
#         for path in myfs.walk.files(filter=['*.html']):
#             cars.append(path)
#         print(f'В обработке: {len(cars)} страниц\n')
#         return cars
#
#
# # ````````````````````````````````````````````````````````````````````
# def replace_result():
#     try:
#         file = 'temp.html'
#         location = 'result_data/'
#         path = os.path.join(location, file)
#         os.remove(path)
#     except FileNotFoundError:
#         pass
#
#     date_ = str(datetime.today())
#
#     try:
#         os.mkdir(f'result_data/{date_[:10]}')
#         source_path = 'result_data/'
#         if os.path.exists(source_path):
#             destination_path = f'{source_path}{date_[:10]}/'
#             filelist = os.listdir(source_path)
#             for item in filelist:
#                 if item.endswith(f'.html'):
#                     os.rename(source_path + item, destination_path + item)
#
#         else:
#             print('Неверный путь к каталогу.')
#
#     except Exception as e:
#         pass
#
#
# # ````разбор страница используя lxml и экспорт в csv``````````````````
# def result_analyse(cars):
#     global all_adv
#     all_adv = []
#
#     numers_item = 0
#
#     for item in cars:
#         item = item.lstrip('/')
#
#         with open(item, 'r', encoding='UTF8') as f:
#             contents = f.read()
#             soup = BeautifulSoup(contents, 'lxml')
#             adv_item = soup.find_all('div', class_='listing-item__wrap')
#
#         for car in adv_item:
#             global cars_detail
#             cars_detail = {}
#
#             # находим ссылку на объявление, обработка ее и добавление в словарь
#             link = car.find('a').get('href')
#             link = 'https://cars.av.by' + link
#             cars_detail['Link'] = link
#
#             # работаем с ценой, получаем в byn и usd
#             price = car.find('div', class_='listing-item__price').text
#             price = price.rstrip('р.')
#             price = price.strip()
#             price = price.replace(' ', '')
#
#             price_usd = car.find('div', class_='listing-item__priceusd').text
#             price_usd = price_usd.strip('≈').rstrip('$')
#             price_usd = price_usd.strip()
#             price_usd = price_usd.replace(' ', '')
#             cars_detail['Price_BYN'] = price
#             cars_detail['Price_USD'] = price_usd
#
#             # получаем модель и марку авто
#             model_cars = car.find('span').text
#             cars_detail['Model'] = model_cars
#
#             # город подачи объявления
#             city = car.find('div', class_='listing-item__location').text
#             cars_detail['City'] = city
#
#             # получаем год выпуска авто, коробка, объем тип кузова
#             params = car.find('div', class_='listing-item__params').text
#             params = params.replace(' ', '')
#             params = params.split('\xa0')
#
#             year_car = params[0]
#             cars_detail['Year'] = year_car
#
#             transmission = params[1]
#             transmission = transmission.lstrip('г.').split(',')
#
#             type_transmission = transmission[0]
#             cars_detail['Type_transmission'] = type_transmission
#
#             vol_drive = transmission[1].strip()
#             cars_detail['Vol_drive'] = vol_drive
#
#             fuel = params[2]
#             fuel = fuel.split(',')
#             type_fuel = fuel[1]
#             cars_detail['Type_fuel'] = type_fuel
#
#             km, type_car = [], []
#             a = ''
#             b = ''
#             for i in str(fuel[2]):
#                 if i.isdigit():
#                     a += i
#                 elif i.isalpha():
#                     b += i
#
#             km.append(int(a))
#             km = km[0]
#
#             type_car.append(b)
#             type_car = type_car[0]
#
#             cars_detail['Km'] = km
#             cars_detail['Type_car'] = type_car
#
#             # номер объявления
#             numers_item = numers_item + 1
#             lnk = cars_detail['Link']
#             print(f'Объявление {numers_item} добавлено в БД для экспорта. {lnk}')
#             all_adv.append(cars_detail)
#     print(f'В БД добавлено {len(all_adv)} объявлений.')
#     return all_adv
#
#
# # использую функцию библиотеки Pandas для сохранения результата в csv
# def pandas_writer(all_adv):
#     df = pd.DataFrame.from_dict(all_adv)
#     df.to_csv('result_data/adv_av_' + print_today + '.csv', encoding='cp1251', index=False)
#
#     date_ = str(datetime.today())
#     shutil.rmtree(f'result_data/{date_[:10]}')
#
#
# # `````сохранение главной страницы для анализа````````````````````````
# def links_starter():
#     req = requests.get(URL)
#     file = open(f'av_main.html', 'w', encoding='UTF8')
#     new_record = req.text
#     file.write(str(new_record))
#     file.close()
#     time.sleep(random.randint(1, 10))
#
#
# # ````функция получение количества объявлений для всех марок`````````
# def count_links():
#     global soup
#     with open('av_main.html', 'r', encoding='UTF8') as f:
#         contents = f.read()
#         soup = BeautifulSoup(contents, 'lxml')
#         count_cars_in_today = soup.find('h1', class_='general-title').text
#
#         print(f'Краткая информация на сегодня {today:%d-%m-%Y} >>> {count_cars_in_today}')
#
#         count_cars_in_today = count_cars_in_today.split()
#         count_car = ''
#         for i in count_cars_in_today:
#             if i.isdigit(): count_car += i
#         count_car = int(count_car)
#         return count_car
#
#
# # ````Краткая информация по автокаталогу``````````````````````````````
# def auto_catalog():
#     cars_info = soup.find_all('a', class_='catalog__link')
#     marks_count = len(cars_info)
#     global pre_info
#     pre_info = {}
#     print(f'Краткая информация на сегодня {today:%d-%m-%Y} >>> {marks_count} марок с доступными объявлениями')
#     print(Style.BRIGHT + Fore.YELLOW + '`' * 70)
#
#     for i in cars_info:
#         car_mark = i.find('span', class_='catalog__title').text
#         car_adv_count = i.find('span', class_='catalog__count').text
#         car_adv_count = car_adv_count.replace(' ', '')
#         pre_info.update({car_mark: car_adv_count})
#
#     n = 1
#     for i, j in pre_info.items():
#         print(f'{n:>4} Марка авто {i:<15} объявлений {j:<10}')
#         n = n + 1
#
#
# # ````````````````````````````````````````````````````````````````````
# def favorites():
#     favorites_dict = {'q': 'https://cars.av.by/bmw/5-seriya', 'w': 'https://cars.av.by/bmw/7-seriya',
#                       'e': 'https://cars.av.by/bmw/3-seriya', 'r': 'https://cars.av.by/audi/a4',
#                       't': 'https://cars.av.by/audi/a6',
#                       'y': 'https://cars.av.by/audi/a3', 'u': 'https://cars.av.by/audi/a5',
#                       'i': 'https://cars.av.by/audi/a8',
#                       'o': 'https://cars.av.by/audi/80', 'p': 'https://cars.av.by/audi/q7',
#                       'a': 'https://cars.av.by/nissan/almera',
#                       's': 'https://cars.av.by/nissan/terrano', 'd': 'https://cars.av.by/nissan/qashqai',
#                       'f': 'https://cars.av.by/nissan/murano',
#                       'g': 'https://cars.av.by/nissan/pathfinder', 'h': 'https://cars.av.by/nissan/primera',
#                       'j': 'https://cars.av.by/nissan/x-trail',
#                       'k': 'https://cars.av.by/renault/kaptur', 'l': 'https://cars.av.by/renault/kadjar',
#                       'z': 'https://cars.av.by/renault/logan',
#                       'x': 'https://cars.av.by/renault/megane', 'c': 'https://cars.av.by/renault/talisman',
#                       'v': 'https://cars.av.by/renault/koleos',
#                       'b': 'https://cars.av.by/renault/duster', 'n': 'https://cars.av.by/renault/arkana',
#                       'vz': 'https://cars.av.by/volkswagen/touran',
#                       'vc': 'https://cars.av.by/volkswagen/touareg', 'vx': 'https://cars.av.by/volkswagen/golf',
#                       'vv': 'https://cars.av.by/volkswagen/sharan',
#                       'vb': 'https://cars.av.by/volkswagen/polo-sedan', 'vn': 'https://cars.av.by/volkswagen/passat',
#                       'vm': 'https://cars.av.by/volkswagen/jetta',
#                       'va': 'https://cars.av.by/volkswagen/tiguan', 'sa': 'https://cars.av.by/skoda/yeti',
#                       'sd': 'https://cars.av.by/skoda/octavia',
#                       'sf': 'https://cars.av.by/skoda/rapid', 'sg': 'https://cars.av.by/skoda/kodiaq',
#                       'mn': 'https://cars.av.by/mercedes-benz/c-klass',
#                       'mb': 'https://cars.av.by/mercedes-benz/gl-klass', 'mv': 'https://cars.av.by/mercedes-benz/vito',
#                       'tv': 'https://cars.av.by/toyota/venza',
#                       'tc': 'https://cars.av.by/toyota/camry', 'ta': 'https://cars.av.by/toyota/avensis',
#                       'tl': 'https://cars.av.by/toyota/corolla',
#                       'tr': 'https://cars.av.by/toyota/land-cruiser',
#                       'tp': 'https://cars.av.by/toyota/land-cruiser-prado',
#                       'vq': 'https://cars.av.by/volvo/v70', 've': 'https://cars.av.by/volvo/v90',
#                       'vr': 'https://cars.av.by/volvo/xc90', 'vt': 'https://cars.av.by/volvo/xc60',
#                       'vy': 'https://cars.av.by/volvo/xc70', 'vo': 'https://cars.av.by/volvo/s80',
#                       'mz': 'https://cars.av.by/mazda/6', 'po': 'https://cars.av.by/peugeot/307',
#                       'pi': 'https://cars.av.by/peugeot/406', 'pu': 'https://cars.av.by/peugeot/407',
#                       'pt': 'https://cars.av.by/peugeot/3008',
#                       'pr': 'https://cars.av.by/peugeot/2008', 'op': 'https://cars.av.by/opel/vectra',
#                       'oi': 'https://cars.av.by/opel/zafira',
#                       'ou': 'https://cars.av.by/opel/astra', 'oy': 'https://cars.av.by/opel/insignia',
#                       'ot': 'https://cars.av.by/opel/mokka', 'oe': 'https://cars.av.by/opel/omega'}
#
#     print(Style.BRIGHT + Fore.RED + 'АВТО ДЛЯ ПАРСИНГА:')
#     print('''
# mv MERCEDES-BENZ VITO   a NISSAN ALMERA     x RENAULT MEGANE            q BMW 5 серии
# mb MERCEDES-BENZ GL     s NISSAN TERRANO    c RENAULT TALISMAN          w BMW 7 серии
# mn MERCEDES-BENZ C      d NISSAN QASHQAI    v RENAULT KOLEOS            e BMW 3 серии
# r AUDI A4               f NISSAN MURANO     b RENAULT DUSTER            sa SKODA YETI
# t AUDI A6               g NISSAN PATHFINDER n RENAULT ARKANA            sd SKODA OCTAVIA
# y AUDI A3               h NISSAN PRIMERA    vz VOLKSWAGEN TOURAN        sf SKODA RAPID
# u AUDI A5               j NISSAN X-TRAIL    vc VOLKSWAGEN TOUAREG       sg SKODA KODIAQ
# i AUDI A8               k RENAULT KAPTUR    vx VOLKSWAGEN GOLF          vn VOLKSWAGEN PASSAT
# o AUDI 80               l RENAULT KAJAR     vv VOLKSWAGEN SHARAN        vm VOLKSWAGEN JETTA
# p AUDI Q7               z RENAULT LOGAN     vb VOLKSWAGEN POLO_SEDAN    va VOLKSWAGEN TIGUAN
# tv TOYOTA VENZA         op OPEL VECTRA      vq VOLVO V70                mz MAZDA 6
# tc TOYOTA CAMRY         oi OPEL ZAFIRA      ve VOLVO V90                po PEUGEOT 307
# ta TOYOTA AVENSIS       ou OPEL ASTRA       vr VOLVO XC90               pi PEUGEOT 406
# tl TOYOTA COROLLA       oy OPEL INSIGNIA    vt VOLVO XC60               pu PEUGEOT 407
# tr TOYOTA LAND-CRUISER  ot OPEL MOKKA       vy VOLVO XC70               pt PEUGEOT 3008
# tp TOYOTA CRUISER-PRADO oe OPEL OMEGA       vo VOLVO S80                pr PEUGEOT 2008
#      ''')
#     user_opt = input('Выберите модель авто (mv)...(pr) или (qq) для выхода >>> ').strip().lower()
#     if user_opt in favorites_dict.keys():
#
#         user_model_links = favorites_dict[user_opt]
#         print(f'Такая марка существует и доступна для парсинга: {user_model_links}. Скачать y / n')
#
#         user_option = input('>>> ').strip().lower()
#         print(Style.BRIGHT + Fore.YELLOW + '`' * 70)
#
#         if user_option == 'y':
#             alpha(user_model_links)
#             # link_download(user_model_links)
#
#
#     elif (user_opt != 'qq') and (user_opt not in favorites_dict.keys()):
#         print('Нет такой марки')
#     elif user_opt == 'qq':
#         main()
#
#
# # ````````````````````````````````````````````````````````````````````
#
#
# def main():
#     while True:
#         print(Style.BRIGHT + Fore.YELLOW + '`' * 70)
#         print(Style.BRIGHT + Fore.YELLOW + '''
#  █████╗ ██╗   ██╗    ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗
# ██╔══██╗██║   ██║    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
# ███████║██║   ██║    ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝
# ██╔══██║╚██╗ ██╔╝    ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗
# ██║  ██║ ╚████╔╝     ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║
# ╚═╝  ╚═╝  ╚═══╝      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
# ''')
#
#         print(Style.BRIGHT + Fore.RED + 'ГЛАВНОЕ МЕНЮ:')
#         print('''1 Краткая сводная информация на сегодня
# 2 Информация о продажах TOP 30 авто
# 3 Избранное авто. Выбор марки и модели для парсинга
# 4 Анализ полученных результатов и сохранение в CSV
# 5 Выход из программы\n''')
#
#         user_option = input('Выберите пункт меню (1)...(5) >>> ').strip()
#         print(Style.BRIGHT + Fore.YELLOW + '`' * 70)
#
#         if user_option == '1':
#             links_starter()
#             count_links()
#
#         elif user_option == '2':
#             count_links()
#             auto_catalog()
#
#         elif user_option == '3':
#             favorites()
#
#         elif user_option == '4':
#             replace_result()
#             control_files()
#             result_analyse(cars)
#             pandas_writer(all_adv)
#
#         elif user_option == '5':
#             break
#
#
# # ```````````````````````````````````````````````````````````````````
# # if __name__ == '__main__':
# #     main()

