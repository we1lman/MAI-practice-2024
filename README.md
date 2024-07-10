# Экспертная система для выбора профиля обучения

Этот проект представляет собой веб-приложение, созданное для помощи абитуриентам в выборе профиля обучения в институте компьютерных наук и прикладной математики. Система учитывает интересы пользователя и результаты ЕГЭ, чтобы предоставить наилучшие рекомендации.

## Установка и запуск

### Требования

- Python 3.8+
- Poetry

### Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/we1lman/MAI-practice-2024
    cd MAI-practice-2024
    ```

2. Установите зависимости с помощью Poetry:

    ```sh
    poetry install
    ```

### Запуск

1. Активируйте виртуальное окружение:

    ```sh
    poetry shell
    ```

2. Запустите Flask приложение:

    ```sh
    poetry run python run.py
    ```

3. Перейдите по адресу [http://127.0.0.1:5001](http://127.0.0.1:5001) в вашем браузере, чтобы увидеть приложение в действии.

## Структура проекта
```
MAI-practice-2024/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── decision_engine.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── questions.html
│   │   └── result.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── data/
│       ├── outcomes.json
│       └── questions.json
├── .gitignore
├── README.md
├── config.py
├── pyproject.lock
├── poetry.toml
└── run.py
```

## Использование

1. На главной странице введите ваши интересы и результаты ЕГЭ.
2. Ответьте на вопросы, которые помогут определить наилучший профиль обучения.
3. Получите рекомендации по профилю обучения и форме обучения.

## Техническое содействие

Проект был создан с техническим содействием ChatGPT, языковой модели от OpenAI. ChatGPT предоставил полезные рекомендации и примеры кода, что помогло в разработке и документировании проекта.

## Вклад

Если вы хотите внести вклад в проект, пожалуйста, сделайте форк репозитория и создайте новую ветку для ваших изменений. После внесения изменений, откройте pull request.
