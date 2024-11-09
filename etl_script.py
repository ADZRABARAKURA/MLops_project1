# -*- coding: utf-8 -*-

import pandas as pd
from s3_utils import download_from_s3, upload_to_s3

# Задаем параметры
bucket_name = "my-dataset"  # Название корзины в S3
raw_data_key = "Titanic.csv"  # Ключ (путь) исходного файла в S3
processed_data_key = "Titanic_processed.csv"  # Ключ для обработанного файла в S3

# Локальные пути для скачивания и сохранения файлов
raw_data_path = r"D:\data\raw\Titanic.csv"
processed_data_path = r"D:\data\processed\Titanic_processed.csv"

# Шаг 1: Скачиваем данные с S3
print("Downloading data from S3...")
download_from_s3(bucket_name, raw_data_key, raw_data_path)

# Шаг 2: Обрабатываем данные (например, фильтруем по возрасту)
print("Processing data...")
df = pd.read_csv(raw_data_path)

# Пример обработки: фильтрация данных, оставляем только пассажиров старше 18 лет
df_filtered = df[df["Age"] > 18]

# Сохраняем обработанные данные в новый файл
df_filtered.to_csv(processed_data_path, index=False)
print(f"Processed data saved to {processed_data_path}")

# Шаг 3: Загружаем обработанные данные обратно в S3
print("Uploading processed data to S3...")
upload_to_s3(bucket_name, processed_data_path, processed_data_key)

print("ETL process completed successfully.")
