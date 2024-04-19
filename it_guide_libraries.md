# Creare libs per il MPCode
> Dalla versione 0.0.1 MPCode supporta le librerie personalizzate - *libs*

## Introduzione
Tutte le libs per MPCode sono create in Python ed esportano le loro funzioni in esso <br>
Per *cose più interessanti* potete usare il codice source del progetto!

## Requisiti per le libs

### funcs.py
Il file funcs.py deve contenere tutte le funzioni che saranno utilizzate in MPCode <br>
I nomi delle funzioni dovrebbero essere i seguenti: `lib_funzione` <br>
Esempio:
- Nome della lib: `mpcmath`
- Funzione: `mpcmath_ex`

Tutte le funzioni e i loro nomi per MPCode devono essere specificati nel python dict `funcs` <br>
Esempio: `funcs = {'ex':mpcmath_ex}`

Nel file dovrebbe esserci anche una variabile `prefix` con il *prefisso* standard delle funzioni della lib <br>
Prefisso - nome breve *prima delle funzioni di una certa lib*, necessario per non confondere le funzioni con lo stesso nome di libs diverse <br>
Il prefisso può essere *qualsiasi* prefisso, ma si consiglia di scrivere un nome di lib breve e di inserire `.` alla fine <br>
Esempio:
- Nome della lib: `mpcmath`
- Prefisso per le funzioni della lib: `math.`
- Come appare l'utilizzo dei comandi di questa lib: `math.function`

**Nota: tutti gli argomenti vengono passati alla funzione come una *python lista*, anche se l'argomento è singolo** <br>
**Raccomandazioni: se è necessario accettare parametri aggiuntivi prima dell'elenco di alcuni argomenti, assegnare loro nomi che iniziano con `~`**

### meta.py
Il file meta.py deve contenere informazioni sulla lib <br>

Un esempio che contiene tutto ciò che serve:

```
# File scaricabili
files = ['funcs.py']

# Nome breve della lib
name = 'mpcmath'

# Versione della lib
version = '0.0.0.1'

# Сreatori
by = 'mrwek & weksoftware'

# Descrizione
description = 'Библиотека для выполнения математических выражений'

# Repository su github
github = 'Mister-Wek/mpcmath'

# Prefisso della lib
prefix = 'math.'

# Versione del MPCode
mpcode_version = '0.0.1'
```

*File scaricabili* - elenco dei file da installare <br>
**Nota: il download di librerie tramite la funzione `get_lib` non supporta la distribuzione dei file in cartelle. Tutti i file si troveranno in un'unica cartella**

*Nome breve della lib* - nome utilizzato nei nomi delle funzioni e con cui MPCode identificherà la lib <br>
**Nota: cercare di rendere il nome unico e di farlo corrispondere al nome del repository su github**

*Versione del MPCode* - Versione del MPCode, su cui è stata sviluppata la lib <br>
**Nota: cercate di sviluppare con la versione più aggiornata**

## Struttura dei repository su Github
Tutti i file di libreria devono trovarsi nella cartella `lib` <br>
Questa cartella deve contenere i file `meta.py` e `funcs.py`

**Raccomandazioni: se la libreria contiene requisti da Python, specificare tali requisti**

## Esempi
- [mpcmath](https://github.com/Mister-Wek/mpcmath)
- [mpcsymbols](https://github.com/Mister-Wek/mpcsymbols)
