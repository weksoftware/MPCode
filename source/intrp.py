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

import funcs


def mpcode_use(args):
    try:
        if args[0] == '~prefix' or args[0] == '~p':
            prefix = args[1]
            args = args[2:]

            for i in args:
                exec(f'from libs.{i} import funcs as {i}; main_funcs.update(funcs.add_to_key({i}.funcs, "{prefix}"))')

        elif args[0] == '~only' or args[0] == '~o':
            lib = args[1]
            args = args[2:]

            for i in args:
                exec(f'from libs.{lib}.funcs import {lib}_{i}; main_funcs.update({{"{i}":{lib}_{i}}})')

        else:
            for i in args:
                exec(f'from libs.{i} import funcs as {i}; main_funcs.update(funcs.add_to_key({i}.funcs, {i}.prefix))')

        return 'success'
    except:
        return 'use error'


main_funcs = { 'use': mpcode_use }
main_funcs.update(funcs.funcs)


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

    new_blocks = blocks

    while n < len(blocks):
        if blocks[n] == '/*':
            e = blocks[n:].index('*/')
            del new_blocks[n:e + n + 1]
            n = e
        n += 1

    blocks = new_blocks
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
    
    elif comands[position] == 'if' and position + 2 <= len(comands) and isinstance(comands[position + 1], list) and isinstance(comands[position + 2], list):
        if run_list(comands[position + 1])[0] == 'true':
            return {
            'result': run_list(comands[position + 2]),
            'end': position + 2
            }

        else:
            return {
            'result': 'false',
            'end': position + 2
            }
        
    elif comands[position] == 'ife' and position + 3 <= len(comands) and isinstance(comands[position + 1], list) and isinstance(comands[position + 2], list) and isinstance(comands[position + 3], list):
        if run_list(comands[position + 1])[0] == 'true':
            return {
            'result': run_list(comands[position + 2]),
            'end': position + 3
            }

        else:
            return {
            'result': run_list(comands[position + 3]),
            'end': position + 3
            }
        
    elif comands[position] == 'fino' and position + 2 <= len(comands) and isinstance(comands[position + 1], list) and isinstance(comands[position + 2], list):
        while run_list(comands[position + 1])[0] == 'true':
            run_list(comands[position + 2])
        
        return {
            'result': 'fino',
            'end': position + 2
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
