## Структура проекта

- **Dockerfile**: Docker-образ для запуска экспериментальных скриптов с Poetry, MLflow и необходимыми зависимостями.
- **docker-compose.yml**: Сценарий для управления несколькими контейнерами: MinIO для хранения данных и MLflow для отслеживания экспериментов.
- **run_experiments.py**: Основной скрипт для запуска экспериментов.
- **config.json**: Конфигурационные параметры для скрипта экспериментов.
- **mlruns/**: Папка для хранения логов MLflow (сохранена на локальном диске через Docker volume).
- **data/**: Папка для хранения данных экспериментов.

## Установка и запуск

### Предварительные требования
- Убедитесь, что у вас установлены **Docker** и **Docker Compose**.

### Клонирование репозитория
1. Клонируйте репозиторий:
   git clone https://github.com/your-repo/MLops_project2.git
   cd MLops_project2
Запуск через Docker Compose
Сначала соберите и запустите все контейнеры с помощью Docker Compose:
docker-compose up --build
Система создаст и запустит следующие контейнеры:

minio: Образ MinIO для хранения данных на S3-совместимом хранилище.
mlflow: MLflow сервер для отслеживания экспериментов.
experiment_runner: Контейнер для выполнения экспериментов с использованием MLflow и MinIO.
После запуска:

MinIO будет доступен на порту 9000 (интерфейс) и 9001 (для доступа API).
MLflow будет доступен на порту 5000 для отслеживания и визуализации экспериментов.
Доступ к MinIO можно получить по адресу: http://localhost:9000 с учетными данными:

Access Key: minioadmin
Secret Key: minioadmin
Доступ к MLflow можно получить по адресу: http://localhost:5000.

Установка зависимостей через Poetry
Если вы хотите работать с проектом локально и установить зависимости через Poetry, выполните следующие шаги:

Установите Poetry:
curl -sSL https://install.python-poetry.org | python3 -
Установите все зависимости:
poetry install --no-dev
Запуск эксперимента вручную
Чтобы вручную запустить эксперименты, используйте следующую команду:
docker-compose run experiment_runner python run_experiments.py --config /app/config.json
Структура Docker Compose
minio
Контейнер для хранения данных с использованием MinIO.

yaml
minio:
  image: minio/minio
  container_name: minio
  ports:
    - "9000:9000"
    - "9001:9001"
  environment:
    MINIO_ROOT_USER: "minioadmin"
    MINIO_ROOT_PASSWORD: "minioadmin"
  command: server /data --console-address ":9001"
  volumes:
    - minio_data:/data
mlflow
Контейнер для запуска MLflow сервера.

yaml
mlflow:
  image: mlflow/mlflow
  container_name: mlflow
  ports:
    - "5000:5000"
  environment:
    MLFLOW_TRACKING_URI: "http://0.0.0.0:5000"
  volumes:
    - ./mlruns:/mlflow/mlruns
experiment_runner
Контейнер для выполнения экспериментов.

yaml
experiment_runner:
  build:
    context: .
    dockerfile: Dockerfile
  container_name: experiment_runner
  depends_on:
    - minio
    - mlflow
  environment:
    AWS_ACCESS_KEY_ID: "minioadmin"
    AWS_SECRET_ACCESS_KEY: "minioadmin"
    MLFLOW_TRACKING_URI: "http://mlflow:5000"
    S3_ENDPOINT_URL: "http://minio:9000"
  volumes:
    - ./data:/app/data
  command: ["python", "run_experiments.py", "--config", "/app/config.json"]