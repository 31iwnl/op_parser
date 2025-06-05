import os
import logging

from src.op_parser import (
    Downloader,
    OpFileParser,
    IAGA2002Downloader,  # импорт нового загрузчика для IAGA
    IAGA2002Parser,
    safe_float,
    f_to_c,
    inch_to_mm,
    mph_to_mps,
    mile_to_km
)

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
    files = downloader.get_files(download=False)
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
    input_folder = 'data'
    output_csv = 'test_output.csv'
    parser.parse_folder_to_csv(input_folder, output_csv)
    if os.path.exists(output_csv):
        print(f"CSV файл успешно создан: {output_csv}")
    else:
        print("Ошибка: CSV файл не создан")


def test_iaga_downloader_and_parser(download=False):
    print("Тестируем загрузку и парсинг IAGA-2002 файлов с сохранением в единый CSV...")

    downloader = IAGA2002Downloader(data_dir='data')

    if download:
        iaga_url = 'https://www2.irf.se/maggraphs/rt_iaga_last_hour_1sec_secondary.txt'
        local_file = downloader.download_file(iaga_url)
        if not local_file:
            print("Не удалось скачать файл, пропускаем тест")
            return
        files_to_parse = [local_file]
    else:
        files_to_parse = downloader.list_local_files()
        if not files_to_parse:
            print("Локальные файлы не найдены, пропускаем тест")
            return

    downloader.parse_files_to_csv(files_to_parse)


if __name__ == '__main__':
    FTP_HOST = 'ftp.ncdc.noaa.gov'
    FTP_DIR = '/pub/data/gsod'

    if FTP_HOST and FTP_DIR:
        test_downloader(FTP_HOST, FTP_DIR)
    else:
        print("FTP параметры не заданы, пропускаем тест скачивания")

    test_local_listing()
    test_parser()

    # Передайте download=False, чтобы использовать локальные файлы вместо скачивания
    test_iaga_downloader_and_parser(download=False)
