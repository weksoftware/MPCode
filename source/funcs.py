#    __  ______  _________  ___  ____
#   /  |/  / _ \/ ___/ __ \/ _ \/ __/
#  / /|_/ / ___/ /__/ /_/ / // / _/  
# /_/  /_/_/   \___/\____/____/___/  
#
# MPCode library
# version 0.1.1
# © weksoftware & mrwek, 2024
# Правообладатель:
# https://weksoftware.ru/
# help@weksoftware.ru
# Information & projects:
# https://discord.gg/eKCgfGJWzG
#

import sys
import requests
import os

version_mpcode = '0.1.1'


def arg_str(args):
    args1 = list()

    for arg in args:
        if type(arg) is str:
            args1.append(arg)

    return args1


# Print для отладки ----------------------------------------------
def print_d(strings = [''], sep = ' ', end = '\n', prefix = 'Debug:'):
    if type(strings) is not list:
        strings = [strings]
    
    print(prefix, end='')

    for string in strings:
        print(string, end=sep)

    print('', end=end)


# Проверка на наличие списка в списке ----------------------------
def list_in(cerca_list):
    r = False
    
    for i in cerca_list:
        if type(i) is list:
            r = True
    
    return r


# Добавление префиксов к ключам ----------------------------------
def add_to_key(old_dict, prefix):
    keys = list(old_dict.keys())
    
    for key in keys:
        old_dict[prefix + key] = old_dict.pop(key)
    
    return old_dict


# Конвертация списка с подсписками в один список -----------------
def uno_list(gruppo):
    r_list = list()
    
    while list_in(gruppo):
        r_list = list()
        
        for i in gruppo:
            if type(i) is list:
                r_list += i
            else:
                r_list.append(i)
                
        gruppo = r_list
        
    if r_list == list():
        r_list = gruppo
        
    return r_list

# Получение метадаты и сохранение в файл -------------------------
def get_meta(url, path='meta_for_get_data.py'):
    r = requests.get(url)
    if r.status_code != '404':
        f = open(path, 'w', encoding='utf-8')
        strings = r.content.decode('utf-8').split('\n')
        for s in strings:
            f.write(s + '\n')
        f.close()


# Проверка строки на возможность конвертации во float ------------
def str_is_float(s):
    try:
        return(float(s))
    except ValueError:
        return(s)


# MPCODE STANDART FUNCTIONS --------------------------------------
def mpcode_b():
    return 'Buongiorno mpcode!'


def mpcode_e():
    sys.exit()


def mpcode_p(args):

    space = ' '

    if args[0] == '~ws' or args[0] == '~without_spaces':
        args = args[1:]
        space = ''

    print(space.join(args))
    
    return args


def mpcode_i(args=['']):
    args = arg_str(args)
    
    return input(' '.join(args))


def mpcode_s(args):
    args = arg_str(args)

    summ = 0

    for n in args:
        summ += int(n)
        
    return str(summ)


def mpcode_m(args):
    args = arg_str(args)

    summ = int(args[0])

    args.pop(0)

    for n in args:
        summ = summ - int(n)
    return str(summ)


def mpcode_w(args=['Введите любое значение для выхода:']):
    return input(' '.join(args))


files_g = None


def mpcode_get_lib(args):
    global files_g

    try:
        for i in args:
            get_meta(f'https://raw.github.com/{i}/main/lib/meta.py')

            lib_name = i[i.index("/") + 1:]

            exec(f'from meta_for_get_data import files as files_{lib_name}; global files_g; files_g = files_{lib_name}', globals())

            files_g += ['meta.py']

            for file in files_g:
                path = f'libs/{lib_name}'

                try:
                    os.makedirs(path)
                except FileExistsError:
                    pass

                get_meta(f'https://raw.github.com/{i}/main/lib/{file}', f'{path}/{file}')
                
            os.remove('meta_for_get_data.py')

        return 'success'
    except:
        return 'get lib error'


def mpcode_libs_info(args = None):
    try:
        if args == None:
            args = os.listdir('libs/')
            
        for lib in args:
            exec(f'from libs.{lib} import meta as metadata')
            print('-------------')
            exec("print(metadata.name); print(f'v{metadata.version}'); print(f'prefix: \"{metadata.prefix}\"'); print(metadata.description); print(f'by {metadata.by}'); print(f'github {metadata.github}')")
        
        return args
    except:
        return 'libs info error'


new_name = None


def mpcode_libs_versions(args = None):
    global new_name
    
    try:
        if args == None:
            args = os.listdir('libs/')
            
        for lib in args:
            exec(f'from libs.{lib} import meta as metadata; global new_name; new_name = metadata.name', globals())
            exec(f"get_meta(f'https://raw.github.com/{{metadata.github}}/main/lib/meta.py', 'meta_for_get_data_{new_name}.py'); import meta_for_get_data_{new_name} as meta_new_{new_name}")
            print('-------------')
            exec(f"print(metadata.name); print(f'v{{metadata.version}}'); print(f'v{{meta_new_{new_name}.version}} current in github'); print(f'github {{metadata.github}}')")
            os.remove(f'meta_for_get_data_{new_name}.py')
        
        return args
    except:
        return 'libs versions error'


def mpcode_version(args=None):
    if args == None:
        print(f'I am MPCode v{version_mpcode} !')
        
        return version_mpcode
    
    elif args[0] == 'github':
        r = requests.get('https://raw.github.com/weksoftware/MPCode/main/version.md')
        print(f'In github.com/weksoftware/MPCode current version {r.content.decode("UTF-8")}')
        
        return r.content.decode('UTF-8')
    

def mpcode_l(args):

    if len(args) == 3: # logic update coming soon...

        from intrp import run_list

        operator = args[1]
        valori = run_list([args[0], args[2]])

        if operator == '=' and str_is_float(valori[0]) == str_is_float(valori[1]):
            return 'true'
        
        elif operator == '!=' and str_is_float(valori[0]) != str_is_float(valori[1]):
            return 'true'
        
        elif operator == '<' and str_is_float(valori[0]) < str_is_float(valori[1]):
            return 'true'
        
        elif operator == '>' and str_is_float(valori[0]) > str_is_float(valori[1]):
            return 'true'
        
        elif operator == '<=' and str_is_float(valori[0]) <= str_is_float(valori[1]):
            return 'true'
        
        elif operator == '>=' and str_is_float(valori[0]) >= str_is_float(valori[1]):
            return 'true'
        
        elif operator == '&' and valori[0] == 'true' and valori[1] == 'true':
            return 'true'
        
        elif operator == '|' and (valori[0] == 'true' or valori[1] == 'true'):
            return 'true'
        
        else:
            return 'false'

    else:
        return 'false'
    
    
def mpcode_line(args):
    return ''.join(args)


def mpcode_numero(args):
    try:
        float(args[0])
        return 'true'
    except:
        return 'false'
    

funcs = {
    'b': mpcode_b,
    'e': mpcode_e,
    'p': mpcode_p,
    'i': mpcode_i,
    's': mpcode_s,
    'm': mpcode_m,
    'w': mpcode_w,
    'get_lib': mpcode_get_lib,
    'libs_info': mpcode_libs_info,
    'libs_versions': mpcode_libs_versions,
    'version': mpcode_version,
    'l': mpcode_l,
    'line':mpcode_line,
    'numero':mpcode_numero
}

