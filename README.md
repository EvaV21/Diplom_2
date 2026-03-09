# Diplom_2
API-тесты Stellar Burgers
Описание

В проекте реализованы автоматизированные тесты API сервиса Stellar Burgers.

Тестирование выполняется с использованием:
pytest
requests
allure-pytest

Отчёт формируется в Allure.

 Проверяемые сценарии
 Создание пользователя

Создание уникального пользователя
Создание пользователя, который уже зарегистрирован
Создание пользователя без одного из обязательных полей

Логин пользователя

Вход под существующим пользователем
Вход с неверным логином и паролем

 Создание заказа

Создание заказа с авторизацией
Создание заказа без авторизации
Создание заказа с ингредиентами
Создание заказа без ингредиентов
Создание заказа с неверным хешем ингредиентов

 Структура проекта
Diplom_2
├── src
│   ├── api.py
│   ├── config.py
│   └── helpers.py
├── tests
│   ├── conftest.py
│   ├── test_create_user.py
│   ├── test_login.py
│   └── test_orders.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

Установка зависимостей

python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

Запуск тестов
pytest

Формирование отчёта Allure

Сбор результатов
pytest --alluredir=allure-results

Просмотр отчёта (если установлен Allure CLI)
allure serve allure-results

Или создание HTML-отчёта:

allure generate allure-results -o allure-report --clean

Результат

Все тесты проходят успешно.
Результаты выполнения тестов отображаются в отчёте Allure.