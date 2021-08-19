# test_Smart_Design

Тестовое задание:
Микросервис для электронного магазина
Модель/cущности:
Товар - отвечает за товар на складе, например - телефон такой-то марки от такого-то производителя.
Поля:
идентификатор (ID)
название
описание
параметры: массив пар ключ/значение

Сущности хранятся в MongoDB на localhost:27017 (можно запускать командой docker run -d -p 27017:27017 mongo)

REST API методы:
Создать новый товар
Получить список названий товаров, с возможностью фильтрации по:
a) названию
b) выбранному параметру и его значению
Получить детали товара по ID
Методы принимают JSON на входе и отдают JSON на выходе.

Разработка микросервиса на любом web framework который больше нравится - например aiohttp, flask, tornado, fastAPI.

В README.md указать:
* Необходимые шаги для инсталляции (напр. pip install -r requirements.txt)
* Команду для запуска сервиса (т.е. python + что-то)
* curl команды с нужными параметрами для прохождения тестового сценария:
* создать товар
* найти его по параметру
* получить детали найденного товара


# Установка
Требуется локально установленная MongoDB (https://docs.mongodb.com/manual/installation/)
GitHub проект:

git clone https://github.com/Jostic-git/shop.git

# Установки

-Необходимые зависимости:

pip install -r requirements.txt

-FastAPI (сервер на 127.0.0.1:8000):

uvicorn main:app --reload

# Создание товара

curl -X POST "http://127.0.0.1:8000/item" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"title\":\"Iphone 13\",\"description\":\"cellphone Iphone\",\"parameters\":[{\"model\":\"13\"},{\"batery\":\"3000\"},{\"os\": \"ios\"},{\"date\": \"20.09.2021\"}]}"

# Получение товара: 
1)по ID

curl -X GET "http://127.0.0.1:8000/item/5fbc06cb11bcf5cbbd8b6c3d" -H  "accept: application/json"

2)Получение товаров по определенным параметрам

curl -X GET "http://127.0.0.1:8000/items/?title=Iphone&description=cellphone&model=13&os=ios" -H  "accept: application/json"

\\title, description - название, всегда присусттвуют у товара.

# Документация

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

\\генерируется сервером
