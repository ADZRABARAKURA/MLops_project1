#!/bin/bash

# Остановка и удаление старых контейнеров
docker-compose down

# Сборка образа для экспериментов
docker-compose build

# Запуск сервисов
docker-compose up -d

# Проверка статуса контейнеров
docker ps

echo "Контейнеры запущены. MinIO доступен по адресу http://localhost:9000, MLFlow - http://localhost:5000"