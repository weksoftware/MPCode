# Скрипт для запуска кода из файла

import intrp

try:
    with open(input('File: '), 'r', encoding="utf-8") as f:
        file = f.read().splitlines()

    while '' in file:
        file.remove('')

    intrp.run(' '.join(file))
except:
    input('Run file error')
