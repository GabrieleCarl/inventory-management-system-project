## Software di un negozio di prodotti vegani

Questo progetto consiste nel realizzare un software per la gestione di un negozio di prodotti vegani. Il software deve avere le seguenti funzionalità:

- Registrare nuovi prodotti, con nome, quantità, prezzo di vendita e prezzo di acquisto.

- Elencare tutti i prodotti presenti.

- Registrare le vendite effettuate.

- Mostrare i profitti lordi e netti.

- Mostrare un menu di aiuto con tutti i comandi disponibili.

Il software è testuale, quindi utilizzabile da riga di comando.

### ESEMPIO DI INTERAZIONE CON IL PROGRAMMA (in grassetto l'input dell'utente)

Inserisci un comando: **aiuto**

I comandi disponibili sono i seguenti:

- aggiungi: aggiungi un prodotto al magazzino

- elenca: elenca i prodotto in magazzino

- vendita: registra una vendita effettuata

- profitti: mostra i profitti totali

- aiuto: mostra i possibili comandi

- chiudi: esci dal programma

--------------------------------------------------------------------------

Inserisci un comando: **aggiungi**

Nome del prodotto: **latte di soia**

Quantità: **20**

Prezzo di acquisto: **0.80**

Prezzo di vendita: **1.40**

AGGIUNTO: 20 X latte di soia

--------------------------------------------------------------------------

Inserisci un comando: **elenca**

PRODOTTO QUANTITA' PREZZO

latte di soia 20 €1.4

tofu 10 €4.19

seitan 5 €5.49

--------------------------------------------------------------------------

Inserisci un comando: **vendita**

Nome del prodotto: **latte di soia**

Quantità: **5**

Aggiungere un altro prodotto ? (si/no): **si**

Nome del prodotto: **tofu**

Quantità: **2**

Aggiungere un altro prodotto ? (si/no): **no**

VENDITA REGISTRATA

- 5 X latte di soia: €1.40

- 2 X tofu: €4.19

Totale: €15.38

--------------------------------------------------------------------------

Inserisci un comando: **profitti**

Profitto: lordo=€42.83 netto=€19.43

--------------------------------------------------------------------------

Inserisci un comando: **storna**

Comando non valido

I comandi disponibili sono i seguenti:

- aggiungi: aggiungi un prodotto al magazzino

- elenca: elenca i prodotto in magazzino

- vendita: registra una vendita effettuata

- profitti: mostra i profitti totali

- aiuto: mostra i possibili comandi

- chiudi: esci dal programma

Inserisci un comando: chiudi

Bye bye
