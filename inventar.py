inventar=[{
    'nume': 'Ford', 
    'cantitate':1, 
    'pret': 10000
}, 
{
    'nume':'Audi', 
    'cantitate':1, 
    'pret': 30000
}]
print(inventar)

# Adăugarea unui nou produs în inventar, care include numele produsului, cantitatea disponibilă și prețul per unitate.

def adauga_produs(nume, cantitate, pret):
    produs= {
    'nume':nume,
    'cantitate': cantitate,
    'pret':pret   
    }
    inventar.append(produs)
    
adauga_produs('Renault', 1, 5000)
print(inventar)

# Creare functie pentru a spune cate produse sunt in inventar

def numar_produse():
    print('Sunt', len(inventar), 'produse in inventar')
    
numar_produse()

# Afișarea listei tuturor produselor din inventar, cu detalii despre nume, cantitate și preț.
def afisare_inventar():
    for p in inventar:
        if p["cantitate"]==1:
            descriere="o masina"
        else:
           descriere= str(p["cantitate"])+ 'masini'
        print(f'Avem {descriere} {p["nume"]} la pret de {p["pret"]}')

afisare_inventar()

# Căutarea unui produs în inventar, după nume, și afișarea informațiilor despre aceasta.

def cauta_produs(nume):
    for p in inventar:
        if p['nume']==nume:
            return p
        return "Produsul nu a fost gasit"
    
print(cauta_produs('Ford'))
print(cauta_produs('Volga'))
