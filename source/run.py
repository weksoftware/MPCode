# Скрипт для запуска кода из терминала

import intrp
import colorama

colorama.init()

while True:
    print(colorama.Back.GREEN + colorama.Fore.WHITE, end='')

    code = input('>>>')
    print(colorama.Back.RESET + colorama.Fore.RESET, end='')

    intrp.run(code)
    print(colorama.Fore.YELLOW + 'Конец выполнения')
