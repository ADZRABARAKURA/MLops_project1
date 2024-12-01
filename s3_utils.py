import boto3
import pickle
import pandas as pd


def download_from_s3(bucket_name, s3_file_path, local_file_path, aws_access_key,
                     aws_secret_key, endpoint_url):
    """Загружает файл из S3."""
    s3 = boto3.client(
        's3',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin',
        endpoint_url='http://localhost:9000'
    )
    s3.download_file(bucket_name, s3_file_path, local_file_path)
    print(f"Файл {s3_file_path} загружен в {local_file_path}.")


def save_model_to_s3(model, bucket_name, s3_file_path, aws_access_key,
                     aws_secret_key, endpoint_url):
    """Сохраняет модель в S3."""
    local_model_path = "model.pkl"
    with open(local_model_path, 'wb') as f:
        pickle.dump(model, f)

    s3 = boto3.client(
        's3',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin',
        endpoint_url='http://localhost:9000'
    )
    s3.upload_file(local_model_path, bucket_name, s3_file_path)
    print(f"Модель сохранена в {bucket_name}/{s3_file_path}.")


def load_csv_from_s3(bucket_name, s3_file_path, aws_access_key,
                     aws_secret_key, endpoint_url):
    """Загружает CSV-файл из S3 и возвращает DataFrame."""
    s3 = boto3.client(
        's3',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin',
        endpoint_url='http://localhost:9000'
    )
    obj = s3.get_object(Bucket=bucket_name, Key=s3_file_path)
    df = pd.read_csv(obj['Body'])
    print(f"Файл {s3_file_path} успешно загружен из S3.")
    return df
