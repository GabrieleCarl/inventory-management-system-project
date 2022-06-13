def gross_profits(): # calcolo profitto lordo
    """
    La funzione gross_profits() ritorna il valore del profitto lordo.
    
    I dati vengono estrapolati dal file record_file.txt.
    """
    with open("record_file.txt", "r", encoding = "utf8") as r_file:
                record_sale = r_file.readlines()
    
    for l in record_sale: # "5 x prodotto: €3.1 @€2.1\n" <- sample row of record_sale
        l=l.strip("\n")
    u = []
    for j in record_sale: # eliminazione delle informazioni superflue
        a = j.split("@")
        b = a[0]
        c = b.split("x")
        d = b.split("€")
        e = float(c[0]) * float(d[-1])
        u.append(e)
    tot_lordi = sum(u)
    return tot_lordi

def cost_purchasing_products(): # calcolo costo acquisto prodotti
    """
    La funzione cost_purchasing_products() ritorna il valore del costo acquisto prodotti venduti.
    
    I dati vengono estrapolati dal file record_file.txt.
    """
    with open("record_file.txt", "r", encoding = "utf8") as r_file:
                record_sale = r_file.readlines()
    
    for l in record_sale: # "5 x prodotto: €3.1 @€2.1\n" <- sample row of record_sale
        l=l.strip("\n")
    k = []
    for j in record_sale: # eliminazione delle informazioni superflue
        a = j.split("@")
        g = a[-1]
        h = g.split("€")        
        b = float(h[-1]) # purchase price
        c = j.split("x")
        d = int(c[0]) # quantità
        f = b*d
        k.append(f)
    tot_costi = sum(k)
    return tot_costi
    
def net_profit(): # mostra profitti netti e lordi
    """
    La funzione net_profit() stampa a schermo i valori di:
        - Profitto lordo
        - Profitto netto (Profitto lordo - costo acquisto prodotti)
    """
    a = gross_profits()
    b = cost_purchasing_products()
    c = a - b
    print(f"Profitto: lordo= €{a:.2f} netto: €{c:.2f}")