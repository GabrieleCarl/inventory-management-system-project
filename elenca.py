import json
import pandas as pd

def itemize():# elenca tutti i prodotti nel magazzino
    """
    La funzione itemize() stampa a schermo una tabella che mostra i prodotti disponibili con quantità e prezzo di acquisto.
    
    La lettura dei dati avviene sul file data_inventory.json, con l'utilizzo della libreria pandas viene creata la tabella.
    """
    with open("data_inventory.json", "r", encoding = "utf8") as json_file:
        inventory = json.load(json_file)
        
    table = pd.DataFrame(
        columns=["Prodotto", "Quantità", "Selling price"])
    # Pandas dataframe per la visualizzazione
    for i in inventory.keys():
        
        tmp = pd.DataFrame(columns=["Prodotto"])
        tmp["Prodotto"] = [i]
        
        for j in inventory[i].keys():
            tmp[j] = [inventory[i][j]]           
        table = table.append(tmp)
    # Stop! l'indentazione va bene!    
    table = table.reset_index(drop=True)
    table = table.set_index("Prodotto")
    table = table.drop(labels=["Purchase price"], axis=1) # Purchase price omitted
    
    from IPython.display import display
    display(table)