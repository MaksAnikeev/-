# Обрезка ссылок с помощью Битли

Проект позволяет создавать в консоли короткие ссылки с помощью сервиса Битли. 
А также считать количество кликов по созданным в Битли коротким ссылкам

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```
Для запуска проекта необходима регистрация на сервисе Bitly
Генерация своего токена в разделе API на сервисе Bitly (Generate token)
Создать в корневом катологе файл .env
Записать в этом файле ваш 
BITLY_TOKEN = '......'

Для запуска через консоль набираете:  
```
python main.py url для сокращения или короткая ссылка для подсчета кликов
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).



# Bitly url shorterer

You can create short links in the console using the Bitley service.
And also you can count the number of clicks on short links created in Bitley

### How to install

Python3 should be already installed. 
Then use `pip` to install dependencies:
```
pip install -r requirements.txt
```
To start the project, you need to register on the Bitly service
Generating your token in the API section on the Bitly service (Generate token)
Create .env file in the root directory
Write in this file your
BITLY_TOKEN = '......'

To run from the console, type:
```
python main.py url to shorten or short link to count clicks
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).