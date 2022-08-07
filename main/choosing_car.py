from bs4 import BeautifulSoup


# ````разбор страница используя lxml и экспорт в csv``````````````````
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
