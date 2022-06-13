import json
import comandi
import elenca

def record_sale(): # registra una vendita
    """
    La funzione record_sale() permette al negozio di registrare una o n vendite effettuate, prendendo come input i seguenti dati:
    - Nome del prodotto (string)
    - Quantità (int)
    
    La registrazione della vendita non è consentita se:
        - Il prodotto non è nel magazzino (data_inventory.json)
        - La quantità richiesta è maggiore di quella disponibile (data_inventory.json)
    
    Al termine della vendita questa viene registrata su record_file.txt
    
    Successivamente viene stampato a schermo il riepilogo della vendita registrata con:
        - Prodotto
        - Quantità
        - Prezzo di vendita unitario
        - Totale € della vendita
        
    Chiarimenti:    
    bb = len_before è la variabile che contiene il numero di righe presenti nel file record_file.txt prima che venga registrata la vendita
    
    Analogamente a quanto sopra:
    aa = len_after è la variabile che contiene il numero di righe presenti nel file record_file.txt dopo che è stata registrata la vendita
    
    In questo modo (len_after-len_before) ho ottenuto quali e quanti records utilizzare per mostrare il riepilogo della vendita.
    
    """
    with open("data_inventory.json", "r", encoding = "utf8") as json_file:
        inventory = json.load(json_file)
    
    with open("record_file.txt", "r", encoding = "utf8") as r_file:
                    len_before = len(r_file.readlines())
    bb = len_before # numero di righe presenti nel file prima della/e vendita/e
        
    n_sale = None
    
    while n_sale != "n":
        
        print("Inserisci il nome del prodotto: ")
        prodotto = None
        prodotto = input()
        prodotto = prodotto.lower()
    
        if prodotto in inventory.keys():
            print("Inserisci la quantità: ")
            quantità = input()
            try:
                tmp = int(quantità)
                temp = int(inventory[prodotto]["Quantità"])
                if temp >= tmp:
                    inventory[prodotto]["Quantità"] = (temp-tmp)

                    with open("record_file.txt", "r", encoding = "utf8") as r_file:
                        len_before = len(r_file.readlines())
                    
                    record1 = f"""{tmp} x {prodotto}: {inventory[prodotto]["Selling price"]} @{inventory[prodotto]["Purchase price"]}\n"""
                # ho aggiunto al record1 anche il @costo del prodotto per 
                # poterlo estrapolare in fase di visualizzazione dei profitti 
                    if inventory[prodotto]["Quantità"] == 0:
                        inventory.pop(prodotto)
               
                    with open("record_file.txt", "a+", encoding = "utf8") as r_file:
                        record_sale = r_file.write(record1)
                
                    print("Vuoi registrare un altro prodotto? (s/n): ")
                    n_sale = input()
                    n_sale = n_sale.lower()
                
                    temp_l = ["s", "n"]
                    while n_sale not in temp_l:                    
                        print("Comando non valido.")                
                        print("Vuoi registrare un altro prodotto? (s/n): ")
                        n_sale = input()
                        n_sale = n_sale.lower()
                      
                else:
                    print("I prodotti presenti non sono abbastanza.")
                    print("I prodotti disponibili sono i seguenti:")
                    elenca.itemize()
                    continue

            except ValueError:
                print("La quantità deve essere un numero intero!")
                comandi.help_user()

        else:
            print("Il prodotto non è disponibile.")
            print("I prodotti disponibili sono i seguenti:")
            elenca.itemize()
    
    with open("record_file.txt", "r", encoding = "utf8") as r_file:
                    len_after = len(r_file.readlines())
    aa = len_after # numero di righe presenti nel file dopo la/e vendita/e
   
    with open("data_inventory.json", "w", encoding = "utf8") as js_file:
        json.dump(inventory, js_file, ensure_ascii=False, indent=4)
    
    d_lun = (bb-aa) # il numero di righe da mostrare in output al termine vendita/e
    
    with open("record_file.txt", "r", encoding = "utf8") as r_file:
                record_sale = r_file.readlines()[d_lun : ] # definizione di quali righe mostrare
            
    print("Vendita registrata:")        
    for l in record_sale: # "5 x prodotto: €3.1 @€2.1\n" <- sample row of record_sale
        l=l.strip("\n")
        l=l.split("@")
        print("-" + f"{l[0]}")
    
    u = []
    for j in record_sale: # "5 x prodotto: €3.1 @€2.1\n" <- sample row of record_sale
        a = j.split("@")
        b = a[0]
        c = b.split("x")
        d = b.split("€") 
        e = float(c[0]) * float(d[-1]) # quantità*prezzo di vendita
        u.append(e)
    tot = sum(u)
            
    print(f"TOTALE: €{tot:.2f}")