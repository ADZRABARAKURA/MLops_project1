1. Установите зависимости: 
   pip install poetry

2. Создайте и активируйте виртуальное окружение: 
   poetry install
   poetry shell

3. Запустите docker файл: 
   docker-compose up -d

4. Проверьте, что MinIO работает: 
   перейдите в браузер и откройте http://localhost:9001. Введите следующие данные для входа:
   Username: minioadmin
   Password: minioadmin
5. Создайте bucket для хранения данных: после входа в интерфейс MinIO,создайте новый бакет с именем, например, my-dataset, в котором будет храниться исходный и обработанный датасет.

6. Скачайте датасет (например, Titanic dataset: https://www.kaggle.com/datasets/brendan45774/test-file?select=tested.csv ) в формате CSV.
Загрузите файл в MinIO: перетащите файл в интерфейс MinIO в созданный бакет my-dataset.

7. Запустите ETL процесс, запустив файл etl_script.py с помощью команды:
   poetry run python etl_script.py

8. Проверьте результаты: после выполнения скрипта новый обработанный файл Titanic_processed.csv будет загружен обратно в S3 в тот же бакет my-dataset

9. Для проверки качества кода и типов используется flake8 и mypy. Эти инструменты настроены для использования с pre-commit hook.

10. Установите pre-commit (если он еще не установлен):
poetry add --dev pre-commit
pre-commit install

11. Запустите pre-commit hook: При каждом коммите будут выполняться проверки стиля кода и типов. Для ручного запуска проверок можно выполнить:
pre-commit run --all-files

12. После всех работ, вы можете остановить контейнер MinIO командой: \
docker-compose down
