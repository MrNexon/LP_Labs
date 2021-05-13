import re

s = input('Строка: ')
print(len(s), len(re.findall(r'(?:^|)([а-яёйА-ЯЁЙA-Za-z]+)(?: |$)', s)))