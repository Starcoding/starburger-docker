# Сайт доставки еды Star Burger

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом.

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)


Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. У всех ресторанов одинаковое меню и одинаковые цены. Просто выберите блюдо из меню на сайте и укажите место доставки. Мы сами найдём ближайший к вам ресторан, всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно выбрать блюда из меню, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы и первым делом созванивается с клиентом, чтобы подтвердить заказ. После оператор выбирает ближайший ресторан и передаёт туда заказ на исполнение. Там всё приготовят и сами доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта. Также сюда заходит менеджер, чтобы обновить меню ресторанов Star Burger.

## Как запустить проект
- Скачайте себе код проекта  
- Установите Docker и Docker Compose
- Создайте ```.env``` файл с переменными среды (подробнее в одноименном пункте ниже)    
- Перейдите в папку с проктом и запустите следующую команду: ```docker-compose up -d --build```
- Проект будет доступен по адресу ```localhost```

## Переменные среды:  

Создать файл `.env` в корневом каталоге со следующими настройками:
- `DEBUG` — дебаг-режим. Поставьте `False`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте. Не стоит использовать значение по-умолчанию, **замените на своё**.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `YANDEX_KEY` — секретный ключ от API Яндекса
- `ROLLBAR_TOKEN` — секретный ключ для доступа к api Rollbar (Данный токен можно не указывать, но тогда не будет работать Rollbar)
- `ROLLBAR_ENVIRONMENT` — Название окружения отображаемого на дашборде Rollbar'а, например: Production server (Данный токен можно не указывать)
- `DATABASE_URL` — строка подключения к БД Postgres в Django, например: postgres://*user*:*password*@db:5432/*название_БД*

## Демо-версия сайта
Сайт собран в Docker образ.
Сайт размещён на Digital Ocean, в качестве веб-сервера выступает nginx, http сервер для Django - Gunicorn.  
IP-адрес сервера: `165.227.153.123`  
User: `root`  
Для подключения к серверу необходим ssh-ключ.  
Сайт подключен к сервису Rollbar (Все ошибки возникающие во время работы сайта, а также деплои, отображаются на специальном дашборде).  


## Деплой
Для установки обновлений, необходимо запустить deploy.sh (Который назодится в каталоге /root/).  
Скрипт самостоятельно скачает последние изменения в коде, соберёт Docker образ и запустит его.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org). За основу был взят код проекта [FoodCart](https://github.com/Saibharath79/FoodCart).

Где используется репозиторий:

- Второй и третий урок [учебного модуля Django](https://dvmn.org/modules/django/)
- Второй урок учебного модуля Docker.