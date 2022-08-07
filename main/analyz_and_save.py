import requests
import random
import time
from bs4 import BeautifulSoup
import math
from fs.osfs import OSFS
import os
from datetime import datetime
import shutil
import pandas as pd
from main import URL



# `````сохранение главной страницы для анализа````````````````````````
def links_starter():
    req = requests.get(URL)
    file = open(f'av_main.html', 'w', encoding='UTF8')
    new_record = req.text
    file.write(str(new_record))
    file.close()
    time.sleep(random.randint(1, 10))

    # ````функция получение количества объявлений и сохранение на диск```
    def alpha(link):
        global n_title

        req = requests.get(link)
        file = open('result_data/temp.html', 'w', encoding='UTF8')
        new_record = req.text
        file.write(str(new_record))
        file.close()
        print(f'Информация о моделе {link} успешна сохранена\n')
        time.sleep(random.randint(1, 3))

        with open('result_data/temp.html', 'r', encoding='UTF8') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'lxml')
            listing_title = soup.find('h3', class_='listing__title').text
            listing_title = listing_title.strip().split()
            n_title = int(listing_title[1])
            print(f'Найдено: {n_title} объявлений')

        num_page = math.ceil(n_title / 25)

        for page in range(1, num_page + 1):
            page_name = 'result_' + str(page) + '.html'
            req = requests.get(link)
            file = open(f'result_data/{page_name}', 'w', encoding='UTF8')
            new_record = req.text
            file.write(str(new_record))
            file.close()
            print(f'Страница: {page_name} успешна сохранена\n')
            time.sleep(random.randint(1, 10))

    # ````проверка наличия файлов в каталоге``````````````````````````````
    def control_files():
        with OSFS("") as myfs:
            work_dir = []
            global cars
            cars = []
            for path in myfs.walk.dirs():
                work_dir.append(path)
            for path in myfs.walk.files(filter=['*.html']):
                cars.append(path)
            print(f'В обработке: {len(cars)} страниц\n')
            return cars

    # ````````````````````````````````````````````````````````````````````
    def replace_result():
        try:
            file = 'temp.html'
            location = 'result_data/'
            path = os.path.join(location, file)
            os.remove(path)
        except FileNotFoundError:
            pass

        date_ = str(datetime.today())

        try:
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

        except Exception as e:
            pass


# использую функцию библиотеки Pandas для сохранения результата в csv
def pandas_writer(all_adv):
    df = pd.DataFrame.from_dict(all_adv)
    df.to_csv('result_data/adv_av_' + print_today + '.csv', encoding='cp1251', index=False)

    date_ = str(datetime.today())
    shutil.rmtree(f'result_data/{date_[:10]}')

