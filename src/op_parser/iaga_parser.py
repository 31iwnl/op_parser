import re


class IAGA2002Parser:
    def __init__(self):
        pass

    def parse_file(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            lines = f.readlines()
        return self.parse_lines(lines)

    def parse_lines(self, lines):
        data = []
        headers = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if not headers:
                # Первая не-комментарий строка — это заголовки
                headers = re.split(r'\s+', line)
                continue
            parts = re.split(r'\s+', line)
            if len(parts) < len(headers):
                continue
            row = dict(zip(headers, parts[:len(headers)]))
            data.append(row)
        return data, headers
