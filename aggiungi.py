import json
import comandi

def add_products(): # aggiungi prodotti al magazzino
    
    """
    La funzione add_products() permette di aggiungere prodotti al magazzino (file data_inventory.json), registrando i dati inseriti dall'utente.
    
    Se il prodotto non è in magazzino (file data_inventory.json), i dati chiesti all'utente sono:
        - nome del prodotto
        - quantità
        - prezzo acquisto (per il negozio)
        - prezzo di vendita (al cliente)
    
    Se il prodotto è già in magazzino (file data_inventory.json) allora permette di incrementarne la quantità, i dati chiesti all'utente sono:
        - nome del prodotto
        - quantità
    in questo caso sia il prezzo di acquisto che il prezzo di vendita sono presenti nel file data_inventory.json
    
    Tipo di dato valido:
        - nome del prodotto = str
        - quantità = int
        - prezzo acquisto = float
        - prezzo di vendita = float 
    """
    
    with open("data_inventory.json", "r", encoding = "utf8") as json_file:
        inventory = json.load(json_file)
    # prodotto(name, quantity, purchase_price, selling_price)
    # name
    print("Inserisci il nome del prodotto: ")
    prodotto = input()
    prodotto = prodotto.lower() 
    if prodotto not in inventory.keys():
        # quantity
        print("Inserisci la quantità: ")
        # check input utente
        try:
            quantità = int(input())
            # purchase_price
            print("Inserisci il prezzo di acquisto senza la valuta €, come da es.(2.71): ")
            prezzo_acquisto = "€"+input()
            # check input utente
            div = prezzo_acquisto.split("€")
            a,b = div
            try:        
                float(b)
                # selling_price
                print("Inserisci il prezzo di vendita senza la valuta €, come da es.(3.14)")
                prezzo_vendita = "€"+input()
                # check input utente
                divis = prezzo_vendita.split("€")
                c,d = divis
                try:        
                    float(d)
                    inventory[prodotto] = {"Quantità" : quantità,                               
                                     "Purchase price" : prezzo_acquisto,
                                      "Selling price" : prezzo_vendita}
                    print(f"Aggiunto: {quantità} x {prodotto}.")
            
                except ValueError as e:
                    print(e)
                    comandi.help_user()
                            
            except ValueError as e:        
                print(e)
                comandi.help_user()
            
        except ValueError:
            print("La quantità deve essere un numero intero!")
            comandi.help_user()
        
    else:
        print("Prodotto già presente, inserisci la quantità da aggiungere: ")
    # check input utente
        try:
            tmp = int(input())
            # quantity update 
            temp = int(inventory[prodotto]["Quantità"])
            inventory[prodotto]["Quantità"] = (tmp+temp)
            print(f"Aggiunto: {tmp} x {prodotto}.")
            
        except ValueError:
            print("La quantità deve essere un numero intero!")
            comandi.help_user()
    

    
    with open("data_inventory.json", "w", encoding = "utf8") as js_file:
        json.dump(inventory, js_file, ensure_ascii=False, indent=4)
        