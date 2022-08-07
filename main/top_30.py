from bs4 import BeautifulSoup
from dateutil.utils import today


# ````функция получение количества объявлений для всех марок`````````
def count_links():
    global soup
    with open('av_main.html', 'r', encoding='UTF8') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        count_cars_in_today = soup.find('h1', class_='general-title').text

        print(f'Краткая информация на сегодня {today:%d-%m-%Y} >>> {count_cars_in_today}')

        count_cars_in_today = count_cars_in_today.split()
        count_car = ''
        for i in count_cars_in_today:
            if i.isdigit(): count_car += i
        count_car = int(count_car)
        return count_car