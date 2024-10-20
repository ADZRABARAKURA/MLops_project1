## Установка окружения

1. Создайте виртуальное окружение: 
   python -m venv venv
   source venv/bin/activate   # Для Linux/Mac
   venv\Scripts\activate      # Для Windows

2. Установите зависимости: 
   pip install -r requirements.txt

3. Инициализируйте pre-commit hook: 
   pre-commit install
