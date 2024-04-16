#    __  ______  _________  ___  ____
#   /  |/  / _ \/ ___/ __ \/ _ \/ __/
#  / /|_/ / ___/ /__/ /_/ / // / _/  
# /_/  /_/_/   \___/\____/____/___/  
#
# MPCode library
# version 0.0.1
# © weksoftware & mrwek, 2024
# Правообладатель:
# https://weksoftware.ru/
# help@weksoftware.ru
# Information & projects:
# https://discord.gg/eKCgfGJWzG
#

import funcs


def mpcode_use(args):
    try:
        for i in args:
            exec(f'from libs.{i} import funcs as {i}; main_funcs.update(funcs.add_to_key({i}.funcs, {i}.prefix))')
            
        return 'success'
    except:
        return 'use error'


main_funcs = {
    'use': mpcode_use,
    'b': funcs.mpcode_b,
    'e': funcs.mpcode_e,
    'p': funcs.mpcode_p,
    'i': funcs.mpcode_i,
    's': funcs.mpcode_s,
    'm': funcs.mpcode_m,
    'w': funcs.mpcode_w,
    'get_lib': funcs.mpcode_get_lib,
    'libs_info': funcs.mpcode_libs_info,
    'libs_versions': funcs.mpcode_libs_versions,
    'version': funcs.mpcode_version
}

variables = dict()


def preparare_gruppo(blocks, start):
    n = start + 1
    blocks[start] = list()

    while n < len(blocks):
        if blocks[n] == '[':
            gruppo = preparare_gruppo(blocks, n)
            blocks[start].append(gruppo['gruppo'])
            blocks[n] = None
            n = gruppo['numero']

        elif blocks[n] == ']':
            blocks[n] = None
            
            return {
                'blocks': blocks,
                'numero': n,
                'gruppo': blocks[start]
            }
        
        else:
            blocks[start].append(blocks[n])
            blocks[n] = None
            
        n += 1


def preparare(code):
    blocks = code.split(' ')
    n = 0

    while n < len(blocks):
        if blocks[n] == '[':
            pre = preparare_gruppo(blocks, n)
            blocks = pre['blocks']
            n = pre['numero']
            
        n += 1

    while None in blocks:
        blocks.remove(None)

    return blocks


def run_list(blocks):
    new_blocks = list()
    i = 0
    
    while i < len(blocks):
        r = run_func(blocks, i)
        new_blocks.append(r['result'])
        i = r['end'] + 1

    return new_blocks


def run_func(comands, position):
    global variables

    if isinstance(comands[position], str) and comands[position] in main_funcs and position < len(comands) - 1 and isinstance(comands[position + 1], list):
        return {
            'result': main_funcs[comands[position]](funcs.uno_list(run_list(comands[position + 1]))),
            'end': position + 1
        }
    
    elif isinstance(comands[position], str) and comands[position] in main_funcs:
        return {
            'result': main_funcs[comands[position]](),
            'end': position
        }
    
    elif isinstance(comands[position], str) and comands[position][0] == '=' and position < len(comands) - 1 and isinstance(comands[position + 1], list):
        rl = funcs.uno_list(run_list(comands[position + 1]))

        if len(rl) == 1:
            variables[comands[position][1:]] = rl[0]
        else:
            variables[comands[position][1:]] = rl

        return {
            'result': variables[comands[position][1:]],
            'end': position + 1
        }

    else:
        if isinstance(comands[position], str) and comands[position] in variables:
            return {
                'result': variables[comands[position]],
                'end': position
            }
        else:
            if comands[position][0] == '\\' and len(comands[position]) > 1:
                return {
                    'result': comands[position][1:],
                    'end': position
                }
            else:
                return {
                    'result': comands[position],
                    'end': position
                }


def run(code):
    comands = preparare(code)
    n = 0

    while n < len(comands):
        n = run_func(comands, n)['end'] + 1
