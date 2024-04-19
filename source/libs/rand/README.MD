# MPCode | Rand

### [[EN](#en)] [[RU](#ru)] [[IT](#it)]

# RU
## Функции:
### gent
**Возвращает `True` с указанным шансом**.\
Аргументы:
- `шанс` (*`integer` или `float`*, необязателен, по умолчанию равен 50)

### gens
**Генерирует строку из случайных символов указанной длины**.\
Аргументы: 
- `длина` (*`integer`*, необязателен, по умолчанию случайное число от 1 до 20)
- `символы` (*`string`*, необязателен, по умолчанию равен маленьким буквам английского алфавита (a-z))

### geni
**Генерирует случайное число (*`integer`*)**.\
Аргументы:
- `от` (*`integer`*, необязателен, по умолчанию равен 0)
- `до` (*`integer`*, необязателен, по умолчанию равен 100)

Если в аргументах указать только одно число (например, `rand.geni[ 50 ]`), то будет сгенерировано число от 0 до указанного числа (в данном случае до 50).


# EN
## Functions:
### gent
**Returns `True` with the specified chance**.\
Argument:
- `chance` (*`integer` or `float`*, optional, default is 50)

### gens
**Generates a string of random characters of the specified length**.\
Arguments: 
- `length` (*`integer`*, optional, default value is a random number between 1 and 20)
- `characters` (*`string`*, optional, default is small letters of the English alphabet (a-z))

### geni
**Generates a random number (*`integer`*)**.\
Arguments:
- `from` (*`integer`*, optional, default is 0)
- `to` (*`integer`*, optional, default is 100)

If you specify only one number in the arguments (e.g., `rand.geni[ 50 ]`), a number from 0 to the specified number (in this case, up to 50) will be generated.


# IT
## Funzioni:
### gent
**Restituisce `true` con la probabilità specificata**.\
Argomenti:
- `probabilità` (*`integer` o `float`*, opzionale, il valore predefinito è 50)

### gens
**Genera una stringa di caratteri casuali della lunghezza specificata**.\
Argomenti:
- `lunghezza` (*`integer`*, opzionale, per impostazione predefinita un numero casuale tra 1 e 20)
- `caratteri` (*`string`*, opzionale, predefinito con lettere minuscole dell'alfabeto latino (a-z))

### geni
**Genera un numero casuale (*`integer`*)**.\
Argomenti:
- `numero minimo` (*`integer`*, opzionale, valore predefinito 0)
- `numero massimo` (*`integer`*, opzionale, valore predefinito 100)

Se si specifica un solo numero negli argomenti (ad esempio, `rand.geni[ 50 ]`), verrà generato un numero da 0 al numero specificato (in questo caso, fino a 50).

