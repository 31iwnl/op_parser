# op_parser

**op_parser** — это мощная и удобная библиотека для скачивания, парсинга и преобразования научных данных из файлов форматов **Op** и **IAGA-2002**.  
Идеально подходит для работы с климатическими и геомагнитными данными, включая данные NOAA и других источников.

---

## 🚀 Возможности

- 📥 Надёжная загрузка файлов по FTP и HTTPS с поддержкой повторных попыток и автоматической распаковкой gzip  
- 📂 Работа с локальными директориями — удобно использовать уже скачанные данные  
- 🔍 Парсинг формата Op с возможностью применять пользовательские функции конвертации единиц измерения  
- 🌐 Универсальный парсер формата IAGA-2002 — стандарт для геомагнитных данных  
- 💾 Экспорт объединённых и преобразованных данных в CSV для анализа и визуализации  

---

## ⚙️ Установка

Установите библиотеку через pip:

pip install op_parser

---

## 💡 Пример использования

### Скачивание и распаковка файлов с FTP

downloader = Downloader(
ftp_host='ftp.ncdc.noaa.gov',
ftp_base_dir='/pub/data/gsod',
data_dir='test_data'
)
files = downloader.get_files(download=True)
print(f"Скачано и распаковано файлов: {len(files)}")

### Работа с локальными файлами

downloader = Downloader(data_dir='data') 
files = downloader.get_files(download=False)
print(f"Найдено локальных .op файлов: {len(files)}")

### Парсинг Op файлов и сохранение в CSV с конвертацией

parser = OpFileParser(
field_converters={
'TemperatureF': [safe_float, f_to_c],
'WindSpeedMph': [safe_float, mph_to_mps],
'PrecipInches': [safe_float, inch_to_mm],
'DistanceMiles': [safe_float, mile_to_km]
},
apply_conversion=True
)
parser.parse_folder_to_csv('data', 'test_output.csv')
print("Данные сохранены в test_output.csv")

### Парсинг файлов формата IAGA-2002

iaga_parser = IAGA2002Parser()
records, headers = iaga_parser.parse_file('data/sample_iaga.txt')
print(f"Прочитано {len(records)} записей с полями: {headers}")

---

## 📄 Лицензия

Проект распространяется под лицензией MIT.

---

## 📬 Контакты и поддержка

Если у вас есть вопросы или предложения, создайте issue на GitHub или свяжитесь с автором по email: xhispeco2018@gmail.com

---

*op_parser — удобный инструмент для работы с научными данными, который помогает быстро и надёжно обрабатывать большие объёмы информации.*