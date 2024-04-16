# Скрипт для запуска кода из файла

import intrp

try:
    with open(input('File: '), 'r', encoding="utf-8") as f:
        file = ' '.join(f.read().splitlines())
    
    intrp.run(file)
except:
    input('Error')
