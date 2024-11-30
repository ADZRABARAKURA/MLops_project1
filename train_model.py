import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from mlflow import log_metric, log_param, start_run
import pandas
#from s3_utils import load_csv_from_s3


def train_and_log_model(config_path, dataset_path, experiment_name):
    """Обучает модель и логирует результаты в MLFlow."""
    # Загрузка конфигурации
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Загрузка данных
    data = pd.read_csv(dataset_path)
    X = data.drop(columns=config['target_column'])
    y = data[config['target_column']]

    # Разделение данных
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Создание и обучение модели
    model = RandomForestClassifier(
        n_estimators=config['n_estimators'],
        max_depth=config['max_depth'],
        max_features=config['max_features'],
        random_state=42
    )
    model.fit(X_train, y_train)

    # Предсказание
    y_pred = model.predict(X_test)

    # Вычисление метрик
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted')
    }

    # Логирование метрик в MLFlow
    with start_run(run_name=experiment_name):
        log_param("n_estimators", config['n_estimators'])
        log_param("max_depth", config['max_depth'])
        log_param("max_features", config['max_features'])
        for metric, value in metrics.items():
            log_metric(metric, value)

    print(f"Результаты эксперимента {experiment_name} залогированы в MLFlow.")

    return model, metrics
