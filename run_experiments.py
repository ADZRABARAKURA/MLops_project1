import json
from itertools import product
from train_model import train_and_log_model
from s3_utils import save_model_to_s3


def run_experiments(config_path, dataset_path, s3_bucket, experiment_name,
                    aws_access_key, aws_secret_key, endpoint_url):
    """Запускает эксперименты с различными гиперпараметрами."""

    # Загрузка конфигурации
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Генерация сетки гиперпараметров
    param_grid = config['param_grid']
    keys, values = zip(*param_grid.items())
    combinations = [dict(zip(keys, v)) for v in product(*values)]

    for i, params in enumerate(combinations):
        experiment_run_name = f"{experiment_name}_run_{i}"
        config.update(params)

        # Сохранение текущей конфигурации
        temp_config_path = "temp_config.json"
        with open(temp_config_path, 'w') as f:
            json.dump(config, f)

        # Обучение и логирование
        model, metrics = train_and_log_model(temp_config_path, dataset_path, experiment_run_name)

        # Сохранение модели в S3
        save_model_to_s3(
            model, s3_bucket, f"{experiment_name}/{experiment_run_name}/model.pkl",
            aws_access_key, aws_secret_key, endpoint_url
        )

    print("Все эксперименты завершены.")
