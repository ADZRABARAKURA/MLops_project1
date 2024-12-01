# Dockerfile для MLFlow
FROM python:3.13-slim

# Установка необходимых библиотек
RUN pip install --no-cache-dir mlflow boto3 scikit-learn pandas

# Установка рабочей директории
WORKDIR /mlflow

# Создание тома для хранения результатов экспериментов
VOLUME /mlflow/mlruns

# Установка инструментов для работы с сетью
RUN apt-get update && apt-get install -y \
    curl \
    iputils-ping \
    && apt-get clean

# Установка Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Копируем проект в контейнер
WORKDIR /app
COPY . /app

# Устанавливаем зависимости проекта
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Команда по умолчанию
ENTRYPOINT ["python", "run_experiments.py"]