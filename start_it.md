# Documentazione iniziale
> MPCode è inguaggio di programmazione interpretato scritto in python

Obiettivi principiali del MPCode: open source e utilizzando un linguaggio di programmazione come costruttore
---
## Introduzione
Tutto in mpcode è un oggetto.\
Ogni oggetto è separato dagli altri da *spazi*

Per *commentare* una parte del codice si può scrivere `/*commento */` (**Commenti devono essere separati da spazi**).

Nota: le parentesi quadre *non sono oggetti separati*, ma combinano altri oggetti in *gruppi di oggetti*.

---
## Gruppi
> Un gruppo è un numero di oggetti combinati in una sequenza all'interno di parentesi quadre.\
All'interno di un gruppo, tutti gli oggetti sono **separati da uno spazio**.
```
[ oggetti alle interno ]
```
Il gruppo **non è un oggetto in sé**.\
`[ 1 2 3 4 5 ]` = `[ 1 2 [ 3 4 5 ] ]` = `[ [ 1 ] 2 3 4 5 ]`...

## Variabili
> Una variabile è un *gruppo* che ha un proprio nome ed è memorizzato in RAM.\
Le variabili possono essere modificate e utilizzate

Per crearle, è necessario scrivere il simbolo `=` e dopo di esso scrivere il nome della variabile

```
=variable1 [ qualsiasi valore ]
```
`variable1` = `[ qualsiasi valore ]`

**Nota: se il gruppo assegnato a una variabile contiene un singolo oggetto, la variabile non viene assegnata al gruppo con l'oggetto, ma all'oggetto *stesso***\
**Se è necessario convertire un gruppo in un singolo oggetto come una riga, utilizzare la funzione `line`**

## Funzione
> Una funzione è un codice python della lib standard mpcode che ha un nome proprio.
Le funzioni possono accettare valori; a tale scopo è necessario inserire un gruppo dopo il nome della funzione.
```
p [ qualsiasi testo ]
```

Ogni funzione restituisce un valore

```
p [ b ]
```
In esempi `b` и `p` è *funzioni*

Nota: molte funzioni standard (tra cui `p`) traducono un gruppo di valori in una singola stringa.

## Libs
> Libs - funzioni disponibili per l'installazione dai repository di github.com\
Le informazioni sulla creazione di liba sono disponibili in [it_guide_libraries.md](it_guide_libraries.md)\
Per installare una lib di terze parti si deve usare la funzione `get_lib`

```
get_lib [nome_utente/nome_del_repository]
```
```
get_lib [ Mister-Wek/mpcmath ]
```
È possibile installare una o più libs.

Per ottenere informazioni sulle libs installate, esiste la funzione `libs_info`, che accetta un gruppo di nomi di libs o nulla (quindi fornisce informazioni su tutte le libs  installate).\
Una funzione simile per ottenere le versioni correnti delle libs installate è `libs_versions`.

Per utilizzare le libs installate, queste devono essere importate durante l'esecuzione del programma.

```
use [ nome_lib ]
```
```
use [ mpcmath ]
p [ math.ex [ 2 + 2 ] ]
```

Affinché le funzioni della lib funzionino, quando le si chiama, il *prefisso* deve essere scritto prima del nome della funzione, che è definito nel file funcs.py di ogni lib.\
Per specificare un prefisso personalizzato, è necessario passare il parametro `~prefix` o `~p` alla funzione come primo argomento.

```
use [ ~p m. mpcmath ]
p [ m.ex [ 2 + 2 ] ]
```

Per collegare singole funzioni di una particolare lib  senza prefisso, usare `~o` o `~solo` seguiti dal nome della lib e da quello della funzione

```
use [ ~o mpcsymbols lq rq ]
p [ lq Citazione di Cesare rq ]
```
Inoltre, le libs *standard* nella cartella `libs` vengono fornite con MPCode a partire dalla versione 0.1.1

Nota: se il download delle funzioni tramite `get_lib` non funziona, provare a specificare un server dns (raccomandiamo Google Public DNS) o abilitare VPN\
Ma si può anche spostare manualmente il contenuto dei repository nella cartella `libs/nome_libreria/`.

## Escaping e argomenti della funzione `p`

La funzione `p` non solo può accettare un gruppo di valori, ma anche il parametro `~ws` come primo argomento.\
Questo parametro rimuove gli spazi tra gli oggetti durante l'output alla console

Per l'escaping di oggetti i cui nomi coincidono con nomi di funzioni, farli precedere dal simbolo `\'.

```
p [ a \b c ]
```

## Operatori logici e funzione `l`
> A partire dalla versione 0.1.0, MPCode supporta gli *operatori logici* all'interno della funzione `l`, che viene utilizzata per confrontare due valori

Operatori logici:
- `=` *uguale a*
- `!=` *non uguale a*
- `<` *minore di*
- `>` *maggiore di*
- `<=` *minore o uguale a*
- `>=` *maggiore o uguale a*
- `&` *e*
- `|` *o*

La funzione `l` prende un gruppo con un'espressione e restituisce `true` / `false`\
Esempio:
```
p [ l [ 2 = 2 ] ]
```

Il suo risultato è utilizzato nelle costruzioni `se`, `ife`, `fino`.

## if, ife, fino

### if
`if` accetta due gruppi di oggetti <br>
Il primo gruppo contiene il risultato `l` (`true`/`false`)\
Il secondo gruppo contiene *il codice da eseguire in caso di `true`*

Esempio:
```
if [ l [ i = hello ] ] [ p [ Hello! ] ]
```

### ife
`ife` accetta tre gruppi di oggetti <br>
I primi due sono gli stessi di `if`, il terzo è il codice che verrà eseguito nel caso di `false`

Esempio:
```
if [ l [ i = hello ] ] [ p [ Hello! ] ] [ p [ Oh D: ] ]
```

### fino
`fino` prende due gruppi, in modo simile a `if`, ma esegue il codice non una volta, ma *fino a* quando `true`

Esempio:
```
fino [ l [ i != exit ] ] [ p [ enter exit per uscire ] ]
```
