import re

st = input('Строка: ')


def words(s: str):
    return ' '.join(re.findall(r'(?:^| )(\w{5})(?: |$)', s))


def words_li(s: str):
    return ' '.join(re.findall(r'(?:^| )(ли\w+)(?: |$)', s, re.IGNORECASE))


def words_lim(s: str):
    return ' '.join(re.findall(r'(?:^| )(\w{5,10})(?: |$)', s))


def words_ov(s: str):
    return ' '.join(re.findall(r'(?:^|)(\w*ов)(?: |$)', s))


print(words(st))
print(words_li(st))
print(words_lim(st))
print(words_ov(st))
