## Парсинг автомобильных объявлений с сайта AV.BY :oncoming_automobile:

```

 █████╗ ██╗   ██╗    ██╗███╗   ██╗███████╗ ██████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██╔══██╗██║   ██║    ██║████╗  ██║██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗
███████║██║   ██║    ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██╔████╔██║█████╗  ██████╔╝
██╔══██║╚██╗ ██╔╝    ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══╝  ██╔══██╗
██║  ██║ ╚████╔╝     ██║██║ ╚████║██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═╝  ╚═══╝      ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                 
```

![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Alba3k/av-parser?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/Alba3k/av-parser?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/Alba3k/av-parser?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Alba3k/av-parser?style=for-the-badge)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/Alba3k/av-parser?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Alba3k/av-parser?style=for-the-badge)
![GitHub followers](https://img.shields.io/github/followers/Alba3k?style=social)


***Парсер для объявлений о продаже автомобилей на сайте 'av.by'. Кодовое имя проекта >>> AV informer :pushpin:***

- :heavy_check_mark: Идея проекта. 
- :heavy_check_mark: Кодовая база, структура кода, написание функций 
- :heavy_check_mark: В данной альфе-версии реализован поиск без вводных данных. На примере BMW пятой серии.
- :heavy_check_mark: Тип экспорта данных: документ формата «.csv» с упорядоченной информацией по каждому объявлению.
- :heavy_check_mark: Вопрос с paginations.
- :hammer_and_wrench: Пользовательское меню.
- :x: Функции: парсинг по маркам авто. 
- :x: Функции: парсинг по моделям авто.  
- :x: Сохранение данных в БД, SQLite3.
- :x: Реализация уведомлений, проработка каналов уведомлений, Telegram, Viber.
- :x: Создание standoline приложения для Windows.
- :hammer_and_wrench: Работа над проектом в середине, пре-релиз и исходный код уже на <code>[**GitHub**](https://github.com/Alba3k/av-parser)</code>

***Краткая информация о работе парсера >>> :books:***

-  Принцип работы парсера: 
    - проверяет количество объявлений по нужной модели на сайте; 
    - скачивает данные для обхода защит сайта; 
    - и из них извлекает информацию о ссылке на объявление, цене (в рублях и долларах), модели и марке, годе выпуска, типе коробки передач, объеме двигателя. 
    - Также извлекает информацию о пробеге и типе кузова. 
    - Полученные данные записываются в табличном формате для дальнейшей статистической обработки или предоставления
    пользователю.

- В теле парсера содержатся следующие функции:
    - загрузчик веб-страниц с исходными данными объявлений в формате html;
    - функция, считывающая общее количество объявлений по нужной модели авто;
    - функция, проверяющая наличие необходимых файлов для последующего разбора и экспорта;
    - функция, считывающая загруженные данные и формирующая словарь с информацией об авто;
    - функция, экспортирующая готовый результат в файл с расширением «.csv».

***Краткая информация о команде разработчиков >>>***

>>> Александр Бабына https://github.com/Alba3k
>>> Екатерина Лесина https://github.com/LesinaKatherine
