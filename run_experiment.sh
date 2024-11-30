#!/bin/bash

# Переменные
CONFIG_FILE=$1  # JSON или YAML файл с гиперпараметрами
EXPERIMENT_NAME=$2  # Название эксперимента

# Читаем параметры из конфигурационного файла
while IFS= read -r line; do
    # Создаем уникальный контейнер для каждого набора параметров
    docker build -f Dockerfile.experiment -t experiment_container .

    # Запускаем контейнер с нужными параметрами
    docker run \
        --name "${EXPERIMENT_NAME}_$(date +%s)" \
        -e PARAMS="$line" \
        experiment_container
done < "$CONFIG_FILE"