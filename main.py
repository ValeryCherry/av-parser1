from datetime import datetime
from bs4 import BeautifulSoup
from fs.osfs import OSFS
from lxml import html
import pandas as pd
import requests
import random
import time
import csv
import math
import os


# ````функция получение количества объявлений````````````````````````
def alpha():
    global listing_title
    with open('result_data/result_1.html', 'r', encoding='UTF8') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        listing_title = soup.find('h3', class_='listing__title').text
        listing_title = listing_title.strip().split()
        listing_title = int(listing_title[1])
        return listing_title

# ````функция сохранения web-страниц на диск``````````````````````````
def link_download():
    tot_count = listing_title
    num_page =  math.ceil(tot_count / 25)
    for page in range(1, num_page + 1):
        page_name = 'result_' + str(page) + '.html'
        req = requests.get(f'https://cars.av.by/filter?brands%5B0%5D%5Bbrand%5D=8&brands%5B0%5D%5Bmodel%5D=5865&brands%5B0%5D%5Bgeneration%5D=4441&page={page}')
        file = open(f'result_data/{page_name}', 'w', encoding='UTF8')


        
        new_record = req.text
        file.write(str(new_record))
        file.close()
        print(f'Страница: {page_name} успешна сохранена\n')
        time.sleep(random.randint(1, 10))

#````проверка наличия файлов в каталоге``````````````````````````````
def control_files():
    with OSFS(".") as myfs:
        work_dir = []
        global cars
        cars = []
        for path in myfs.walk.dirs():
            work_dir.append(path)
        for path in myfs.walk.files(filter=['*.html']):
            cars.append(path)
        print(f'В обработке: {len(cars)} страниц\n')
        return cars

#````````````````````````````````````````````````````````````````````
def replace_result():
    date_ = str(datetime.today())
    os.mkdir(f'result_data/{date_[:10]}')

    source_path = 'result_data/'

    if os.path.exists(source_path):
        destination_path = f'{source_path}{date_[:10]}/'
        filelist = os.listdir(source_path)
        for item in filelist:
                if item.endswith(f'.html'):
                    os.rename(source_path + item, destination_path + item)
        
    else:
        print('Неверный путь к каталогу.')

#````разбор страница используя lxml и экспорт в csv``````````````````
def result_analyse(cars):
    global all_adv
    all_adv = []

    numers_item = 0
    
    for item in cars:
        item = item.lstrip('/')

        with open(item, 'r', encoding='UTF8') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'lxml')
            adv_item = soup.find_all('div', class_='listing-item__wrap')

        for car in adv_item:
            global cars_detail
            cars_detail = {}

    # находим ссылку на объявление, обработка ее и добавление в словарь
            link = car.find('a').get('href')
            link = 'https://cars.av.by' + link
            cars_detail['Link'] = link

    # работаем с ценой, получаем в byn и usd
            price = car.find('div', class_='listing-item__price').text
            price = price.rstrip('р.')
            price = price.strip()
            price = price.replace(' ', '')

            price_usd = car.find('div', class_='listing-item__priceusd').text
            price_usd = price_usd.strip('≈').rstrip('$')
            price_usd = price_usd.strip()
            price_usd = price_usd.replace(' ', '')
            cars_detail['Price_BYN'] = price
            cars_detail['Price_USD'] = price_usd

    # получаем модель и марку авто
            model_cars = car.find('span').text
            cars_detail['Model'] = model_cars
        
    # город подачи объявления
            city = car.find('div', class_='listing-item__location').text
            cars_detail['City'] = city

    # получаем год выпуска авто, коробка, объем тип кузова
            params = car.find('div', class_='listing-item__params').text
            params = params.replace(' ', '')
            params = params.split('\xa0')

            year_car = params[0]
            cars_detail['Year'] = year_car

            transmission = params[1]
            transmission = transmission.lstrip('г.').split(',')

            type_transmission = transmission[0]
            cars_detail['Type_transmission'] = type_transmission
        
            vol_drive = transmission[1].strip()
            cars_detail['Vol_drive'] = vol_drive

            fuel = params[2]
            fuel = fuel.split(',')
            type_fuel = fuel[1]
            cars_detail['Type_fuel'] = type_fuel

            km, type_car = [], []
            a = ''
            b = ''
            for i in str(fuel[2]):
                if i.isdigit():
                    a += i
                elif i.isalpha():
                    b += i

            km.append(int(a))
            km = km[0]

            type_car.append(b)
            type_car = type_car[0]

            cars_detail['Km'] = km
            cars_detail['Type_car'] = type_car

    # номер объявления
            numers_item = numers_item + 1
            lnk = cars_detail['Link']
            print(f'Объявление {numers_item} добавлено в БД для экспорта. {lnk}')
            all_adv.append(cars_detail)

    print(f'В БД добавлено {len(all_adv)} объявлений.')

    return all_adv

    # использую функцию библиотеки Pandas для сохранения результата в csv
def pandas_writer(all_adv):
    df = pd.DataFrame.from_dict(all_adv) 
    df.to_csv('result_data/adv_av.csv',encoding='cp1251', index = False)



# `````````Главная функция ``````````````````````````````````````````
def main():
    # alpha()
    # link_download()
    control_files()
    # replace_result()
    result_analyse(cars)
    pandas_writer(all_adv)

 

# ```````````````````````````````````````````````````````````````````
if __name__ == '__main__':
    main()


