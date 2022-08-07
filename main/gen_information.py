# ````Краткая информация по автокаталогу``````````````````````````````
def auto_catalog():
    cars_info = soup.find_all('a', class_='catalog__link')
    marks_count = len(cars_info)
    global pre_info
    pre_info = {}
    print(f'Краткая информация на сегодня {today:%d-%m-%Y} >>> {marks_count} марок с доступными объявлениями')
    print(Style.BRIGHT + Fore.YELLOW + '`' * 70)

    for i in cars_info:
        car_mark = i.find('span', class_='catalog__title').text
        car_adv_count = i.find('span', class_='catalog__count').text
        car_adv_count = car_adv_count.replace(' ', '')
        pre_info.update({car_mark: car_adv_count})

    n = 1
    for i, j in pre_info.items():
        print(f'{n:>4} Марка авто {i:<15} объявлений {j:<10}')
        n = n + 1


# ````````````````````````````````````````````````````````````````````
def favorites():
    favorites_dict = {'q': 'https://cars.av.by/bmw/5-seriya', 'w': 'https://cars.av.by/bmw/7-seriya',
                      'e': 'https://cars.av.by/bmw/3-seriya', 'r': 'https://cars.av.by/audi/a4',
                      't': 'https://cars.av.by/audi/a6',
                      'y': 'https://cars.av.by/audi/a3', 'u': 'https://cars.av.by/audi/a5',
                      'i': 'https://cars.av.by/audi/a8',
                      'o': 'https://cars.av.by/audi/80', 'p': 'https://cars.av.by/audi/q7',
                      'a': 'https://cars.av.by/nissan/almera',
                      's': 'https://cars.av.by/nissan/terrano', 'd': 'https://cars.av.by/nissan/qashqai',
                      'f': 'https://cars.av.by/nissan/murano',
                      'g': 'https://cars.av.by/nissan/pathfinder', 'h': 'https://cars.av.by/nissan/primera',
                      'j': 'https://cars.av.by/nissan/x-trail',
                      'k': 'https://cars.av.by/renault/kaptur', 'l': 'https://cars.av.by/renault/kadjar',
                      'z': 'https://cars.av.by/renault/logan',
                      'x': 'https://cars.av.by/renault/megane', 'c': 'https://cars.av.by/renault/talisman',
                      'v': 'https://cars.av.by/renault/koleos',
                      'b': 'https://cars.av.by/renault/duster', 'n': 'https://cars.av.by/renault/arkana',
                      'vz': 'https://cars.av.by/volkswagen/touran',
                      'vc': 'https://cars.av.by/volkswagen/touareg', 'vx': 'https://cars.av.by/volkswagen/golf',
                      'vv': 'https://cars.av.by/volkswagen/sharan',
                      'vb': 'https://cars.av.by/volkswagen/polo-sedan', 'vn': 'https://cars.av.by/volkswagen/passat',
                      'vm': 'https://cars.av.by/volkswagen/jetta',
                      'va': 'https://cars.av.by/volkswagen/tiguan', 'sa': 'https://cars.av.by/skoda/yeti',
                      'sd': 'https://cars.av.by/skoda/octavia',
                      'sf': 'https://cars.av.by/skoda/rapid', 'sg': 'https://cars.av.by/skoda/kodiaq',
                      'mn': 'https://cars.av.by/mercedes-benz/c-klass',
                      'mb': 'https://cars.av.by/mercedes-benz/gl-klass', 'mv': 'https://cars.av.by/mercedes-benz/vito',
                      'tv': 'https://cars.av.by/toyota/venza',
                      'tc': 'https://cars.av.by/toyota/camry', 'ta': 'https://cars.av.by/toyota/avensis',
                      'tl': 'https://cars.av.by/toyota/corolla',
                      'tr': 'https://cars.av.by/toyota/land-cruiser',
                      'tp': 'https://cars.av.by/toyota/land-cruiser-prado',
                      'vq': 'https://cars.av.by/volvo/v70', 've': 'https://cars.av.by/volvo/v90',
                      'vr': 'https://cars.av.by/volvo/xc90', 'vt': 'https://cars.av.by/volvo/xc60',
                      'vy': 'https://cars.av.by/volvo/xc70', 'vo': 'https://cars.av.by/volvo/s80',
                      'mz': 'https://cars.av.by/mazda/6', 'po': 'https://cars.av.by/peugeot/307',
                      'pi': 'https://cars.av.by/peugeot/406', 'pu': 'https://cars.av.by/peugeot/407',
                      'pt': 'https://cars.av.by/peugeot/3008',
                      'pr': 'https://cars.av.by/peugeot/2008', 'op': 'https://cars.av.by/opel/vectra',
                      'oi': 'https://cars.av.by/opel/zafira',
                      'ou': 'https://cars.av.by/opel/astra', 'oy': 'https://cars.av.by/opel/insignia',
                      'ot': 'https://cars.av.by/opel/mokka', 'oe': 'https://cars.av.by/opel/omega'}

    print(Style.BRIGHT + Fore.RED + 'АВТО ДЛЯ ПАРСИНГА:')
    print('''
mv MERCEDES-BENZ VITO   a NISSAN ALMERA     x RENAULT MEGANE            q BMW 5 серии
mb MERCEDES-BENZ GL     s NISSAN TERRANO    c RENAULT TALISMAN          w BMW 7 серии
mn MERCEDES-BENZ C      d NISSAN QASHQAI    v RENAULT KOLEOS            e BMW 3 серии
r AUDI A4               f NISSAN MURANO     b RENAULT DUSTER            sa SKODA YETI
t AUDI A6               g NISSAN PATHFINDER n RENAULT ARKANA            sd SKODA OCTAVIA
y AUDI A3               h NISSAN PRIMERA    vz VOLKSWAGEN TOURAN        sf SKODA RAPID
u AUDI A5               j NISSAN X-TRAIL    vc VOLKSWAGEN TOUAREG       sg SKODA KODIAQ 
i AUDI A8               k RENAULT KAPTUR    vx VOLKSWAGEN GOLF          vn VOLKSWAGEN PASSAT
o AUDI 80               l RENAULT KAJAR     vv VOLKSWAGEN SHARAN        vm VOLKSWAGEN JETTA
p AUDI Q7               z RENAULT LOGAN     vb VOLKSWAGEN POLO_SEDAN    va VOLKSWAGEN TIGUAN
tv TOYOTA VENZA         op OPEL VECTRA      vq VOLVO V70                mz MAZDA 6
tc TOYOTA CAMRY         oi OPEL ZAFIRA      ve VOLVO V90                po PEUGEOT 307
ta TOYOTA AVENSIS       ou OPEL ASTRA       vr VOLVO XC90               pi PEUGEOT 406
tl TOYOTA COROLLA       oy OPEL INSIGNIA    vt VOLVO XC60               pu PEUGEOT 407
tr TOYOTA LAND-CRUISER  ot OPEL MOKKA       vy VOLVO XC70               pt PEUGEOT 3008
tp TOYOTA CRUISER-PRADO oe OPEL OMEGA       vo VOLVO S80                pr PEUGEOT 2008
     ''')
    user_opt = input('Выберите модель авто (mv)...(pr) или (qq) для выхода >>> ').strip().lower()
    if user_opt in favorites_dict.keys():

        user_model_links = favorites_dict[user_opt]
        print(f'Такая марка существует и доступна для парсинга: {user_model_links}. Скачать y / n')

        user_option = input('>>> ').strip().lower()
        print(Style.BRIGHT + Fore.YELLOW + '`' * 70)

        if user_option == 'y':
            alpha(user_model_links)
            # link_download(user_model_links)


    elif (user_opt != 'qq') and (user_opt not in favorites_dict.keys()):
        print('Нет такой марки')
    elif user_opt == 'qq':
        main()


# ````````````````````````````````````````````````````````````````````


def main():
    while True:
        print(Style.BRIGHT + Fore.YELLOW + '`' * 70)
        print(Style.BRIGHT + Fore.YELLOW + ''' 
 █████╗ ██╗   ██╗    ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗ 
██╔══██╗██║   ██║    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
███████║██║   ██║    ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝
██╔══██║╚██╗ ██╔╝    ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗
██║  ██║ ╚████╔╝     ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║
╚═╝  ╚═╝  ╚═══╝      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
''')

        print(Style.BRIGHT + Fore.RED + 'ГЛАВНОЕ МЕНЮ:')
        print('''1 Краткая сводная информация на сегодня     
2 Информация о продажах TOP 30 авто         
3 Избранное авто. Выбор марки и модели для парсинга
4 Анализ полученных результатов и сохранение в CSV
5 Выход из программы\n''')

        user_option = input('Выберите пункт меню (1)...(5) >>> ').strip()
        print(Style.BRIGHT + Fore.YELLOW + '`' * 70)

        if user_option == '1':
            links_starter()
            count_links()

        elif user_option == '2':
            count_links()
            auto_catalog()

        elif user_option == '3':
            favorites()

        elif user_option == '4':
            replace_result()
            control_files()
            result_analyse(cars)
            pandas_writer(all_adv)

        elif user_option == '5':
            break


# ```````````````````````````````````````````````````````````````````