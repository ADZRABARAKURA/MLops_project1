import boto3
from botocore.exceptions import NoCredentialsError, ClientError


# Функция для скачивания файла из S3
def download_from_s3(bucket_name, s3_key, download_path):
    # Создаем клиент для S3
    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',  # для MinIO
        aws_access_key_id='minioadmin',        # ключ MinIO
        aws_secret_access_key='minioadmin',    # секрет MinIO
    )
    try:
        # Скачиваем файл
        s3.download_file(bucket_name, s3_key, download_path)
        print(f"File {s3_key} downloaded to {download_path}.")
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"Error downloading file: {e}")


# Функция для загрузки файла в S3
def upload_to_s3(bucket_name, file_path, s3_key):
    # Создаем клиент для S3
    s3 = boto3.client(
        's3',
        endpoint_url='http://localhost:9000',  # для MinIO
        aws_access_key_id='minioadmin',        # ключ MinIO
        aws_secret_access_key='minioadmin',    # секрет MinIO
    )
    try:
        # Загружаем файл
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File {file_path} uploaded to {s3_key}.")
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"Error uploading file: {e}")
