FROM python:3.13-slim  
# Обновляем до нужной версии Python

# Установка необходимых библиотек
RUN pip install --no-cache-dir mlflow boto3

# Установка рабочей директории
WORKDIR /mlflow

# Создание тома для хранения результатов экспериментов
VOLUME /mlflow/mlruns

# Запуск MLFlow сервера
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean

# Копируем проект в контейнер
WORKDIR /app
COPY . /app

# Устанавливаем зависимости проекта
RUN /root/.local/bin/poetry config virtualenvs.create false && /root/.local/bin/poetry install --no-dev

# Команда по умолчанию
ENTRYPOINT ["python", "run_experiments.py"]