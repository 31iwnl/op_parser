import os
import logging

from src.op_parser import Downloader, OpFileParser, safe_float, f_to_c, inch_to_mm, mph_to_mps, mile_to_km

logging.basicConfig(level=logging.INFO)


def test_downloader(ftp_host, ftp_dir):
    print("Тестируем скачивание и распаковку файлов с FTP...")
    downloader = Downloader(ftp_host=ftp_host, ftp_base_dir=ftp_dir, data_dir='test_data')
    files = downloader.get_files(download=True)
    print(f"Скачано и распаковано файлов: {len(files)}")
    for f in files:
        print(f"  - {f}")


def test_local_listing():
    print("Тестируем список локальных файлов в папке data...")
    downloader = Downloader(data_dir='data')
    files = downloader.get_files(download=False)  # берём локальные файлы False, для загрузки True
    print(f"Найдено локальных .op файлов: {len(files)}")
    for f in files:
        print(f"  - {f}")


def test_parser():
    print("Тестируем парсер .op файлов и сохранение в CSV...")
    parser = OpFileParser(
        field_converters={
            'TemperatureF': [safe_float, f_to_c],
            'WindSpeedMph': [safe_float, mph_to_mps],
            'PrecipInches': [safe_float, inch_to_mm],
            'DistanceMiles': [safe_float, mile_to_km]
        },
        apply_conversion=True
    )
    input_folder = 'data'  # папка с локальными файлами
    output_csv = 'test_output.csv'
    parser.parse_folder_to_csv(input_folder, output_csv)
    if os.path.exists(output_csv):
        print(f"CSV файл успешно создан: {output_csv}")
    else:
        print("Ошибка: CSV файл не создан")


if __name__ == '__main__':
    # Замените на реальные FTP параметры для теста скачивания
    FTP_HOST = 'ftp.ncdc.noaa.gov'
    FTP_DIR = '/pub/data/gsod'

    # Тест скачивания (если FTP параметры заданы)
    if FTP_HOST and FTP_DIR:
        test_downloader(FTP_HOST, FTP_DIR)
    else:
        print("FTP параметры не заданы, пропускаем тест скачивания")

    # Тест локального списка файлов
    test_local_listing()

    # Тест парсера и конвертации
    test_parser()
