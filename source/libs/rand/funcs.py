import random
import string

prefix = 'rand.'


def mpcrand_gent(args: list[str] | None = None):
    chance = 50
    
    if args is not None:
        try:
            chance = float(args[0])
        except:
            pass
        
    n = random.uniform(0, 100)
    print(n)
    return str(n <= chance)


def mpcrand_gens(args: list[str] | None = None):
    if args is None:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 20)))
    
    if len(args) == 1:
        if args[0].isdigit():
            return ''.join(random.choice(string.ascii_lowercase) for _ in range(int(args[0])))
        else:
            return ''.join(random.choice(args[0]) for _ in range(random.randint(1, 20)))
    
    else:
        if args[0].isdigit() and not args[1].isdigit():
            return ''.join(random.choice(args[1]) for _ in range(int(args[0])))
        elif not args[0].isdigit() and args[1].isdigit():
            return ''.join(random.choice(args[0]) for _ in range(int(args[1])))
        else:
            return "Invalid arguments"

def mpcrand_geni(nums: list[str] | None = None):
    if nums is None:
        return str(random.randint(0, 100))
    
    mi: int | None = None
    ma: int | None = None
    
    if nums[0].isdigit():
        mi = int(nums[0])
    if len(nums) >= 2 and nums[1].isdigit():
        ma = int(nums[1])
    
    if mi == None:
        return "arguments must be integer"
    elif ma == None:
        return str(random.randint(0, mi))
    else:
        return str(random.randint(mi, ma))


funcs = {
    'geni': mpcrand_geni,
    'gens': mpcrand_gens,
    'gent': mpcrand_gent
}