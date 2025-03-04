import random
#1
dizionario={
    "Mario Rossi": [("antipasti", (8, 7, 9), "Junior Chef"), ("primi", (7, 8, 8), "Junior Chef"), ("secondi", (9, 9, 8), "Junior Chef"), ("dessert", (8, 8, 9), "Junior Chef")],
    "Luigi Bianchi": [("antipasti", (7, 7, 8), "Senior Chef"), ("primi", (8, 9, 7), "Senior Chef"), ("secondi", (7, 8, 7), "Senior Chef"), ("dessert", (9, 8, 8), "Senior Chef")],
    "Giulia Verdi": [("antipasti", (9, 8, 8), "Junior Chef"), ("primi", (8, 7, 9), "Junior Chef"), ("secondi", (8, 8, 8), "Junior Chef"), ("dessert", (7, 9, 8), "Junior Chef")]
}

#2
dizionario["Christian Bandera"]=[
    ("antipasti", (8, 7, 9), 
     "Junior Chef"), 
     ("primi", (7, 2, 8), "Junior Chef"), 
     ("secondi", (9, 9, 8), "Junior Chef"),
    ("dessert", (8, 8, 9), "Junior Chef")]


#3
def nuovaCategoria():
    for nome, dati in dizionario.items():
        for dato in dati:
            tipoPiatto, (num1, num2, num3), categoriaChef = dato
            n1=random.randint(1,10)
            n2=random.randint(1,10)
            n3=random.randint(1,10)
            lista=[]
            if(categoriaChef=="Junior Chef"):
                lista.append(("piatti unici", (n1, n2, n3), "Junior Chef"))
            elif(categoriaChef=="Senior Chef"):
                lista.append(("piatti unici", (n1, n2, n3), "Senior Chef"))
        dizionario[nome].append(lista)
            

#4
def stampaChef(nomeChef):
    if(nomeChef in dizionario):
        for nome, dati in dizionario.items():
            if(nome==nomeChef):
                for dato in dati:
                    tipoPiatto, (num1, num2, num3), categoriaChef = dato
                    print(f"Nome e cognome: {nome}")
                    print(f"Categoria di chef: {categoriaChef}")
                    print(f"Categoria piatto: {tipoPiatto}")
                    print(f"Creatività: {num1}")
                    print(f"Gusto: {num2}")
                    print(f"Presentazione: {num3}")
    else:
        print("Chef non presente")



#5
def datiPiatto(tipoPiattoInserito):
    if(tipoPiattoInserito!="antipasti" and tipoPiattoInserito!="primi" and tipoPiattoInserito!="secondi" and tipoPiattoInserito!="dessert" and tipoPiattoInserito!="piatti unici"):
                print("Categoria piatto non esistente")
    else:
        for nome, dati in dizionario.items():
            for dato in dati:
                tipoPiatto, (num1, num2, num3), categoriaChef = dato
                if(tipoPiattoInserito==tipoPiatto):
                    print(f"Nome e cognome: {nome}")
                    print(f"Categoria di chef: {categoriaChef}")
                    print(f"Creatività: {num1}")
                    print(f"Gusto: {num2}")
                    print(f"Presentazione: {num3}")

#6.1
def totaleMassimo(dizionario, categoriaPiattoInserito, categoriaChefInserito):
    if((categoriaPiattoInserito not in dizionario) and (categoriaChefInserito not in dizionario)):
        print("Dati inseriti in modo errato")
    else:
        massimo=0
        totale=0
        print(f"Chef che hanno conseguito il maggior punteggio nella categoria{categoriaChefInserito}, nei piatti {categoriaPiattoInserito}")
        for nome, dati in dizionario.items():
            for dato in dati:
                tipoPiatto, (num1, num2, num3), categoriaChef = dato
                if(categoriaPiattoInserito==tipoPiatto and categoriaChefInserito==categoriaChef):
                    totale+= num1 + num2 + num3
                    if(totale>massimo):
                        massimo=totale
        
        for nome, dati in dizionario.items():
            for dato in dati:
                tipoPiatto, (num1, num2, num3), categoriaChef = dato
                if(categoriaPiattoInserito==tipoPiatto and categoriaChefInserito==categoriaChef):
                    totale+= num1 + num2 + num3
                    if(totale==massimo):
                        print(nome)

#6.2
def media(dizionario, categoriaPiattoInserito, categoriaChefInserito):
    print(f"Media punteggio nella categoria{categoriaChefInserito}, nei piatti {categoriaPiattoInserito}")
    if((categoriaPiattoInserito not in dizionario) and (categoriaChefInserito not in dizionario)):
        print("Dati inseriti in modo errato")
    else:
        somma=0
        conta=0
        print(f"Chef che hanno conseguito il maggior punteggio nella categoria{categoriaChefInserito}, nei piatti {categoriaPiattoInserito}")
        for nome, dati in dizionario.items():
            for dato in dati:
                tipoPiatto, (num1, num2, num3), categoriaChef = dato
                if(categoriaPiattoInserito==tipoPiatto and categoriaChefInserito==categoriaChef):
                    numDaSommare=(num1+num2+num3)
                    somma+=numDaSommare
                    conta+=1
        media= somma/conta
        print(media)

#7
def inserisci_dati_nuovo_chef():


    for i in range(5):
        creativita=int(input("Inserire punteggio creativita: "))
        while creativita<0:
            creativita=int(input("Inserire punteggio creativita: "))

        gusto=int(input("Inserire punteggio gusto: "))
        while gusto<0:
            gusto=int(input("Inserire punteggio gusto: "))

        presentazione=int(input("Inserire punteggio presentazione: "))
        while presentazione<0:
            presentazione=int(input("Inserire punteggio presentazione: "))
    
    

def inserisci_nuovo_chef():
    nome=input("Inserisci il nome: ")
    while nome=="":
        nome=input("Inserisci il nome: ")
    
    cognome=input("Inserisci cognome: ")
    while cognome=="":
        cognome=input("Inserisci cognome: ")
    nominativo= nome+" "+cognome

    categoriaChef=input("inserisci la categoria dello chef: ")
    while(categoriaChef=="" or categoriaChef!="Junior Chef" or categoriaChef!="Senior Chef"):
        categoriaChef=input("inserisci la categoria dello chef: ")

    dizionario[nominativo]=[]
    for i in range(5):
        creativita=int(input("Inserire punteggio creativita: "))
        while creativita<0:
            creativita=int(input("Inserire punteggio creativita: "))

        gusto=int(input("Inserire punteggio gusto: "))
        while gusto<0:
            gusto=int(input("Inserire punteggio gusto: "))

        presentazione=int(input("Inserire punteggio presentazione: "))
        while presentazione<0:
            presentazione=int(input("Inserire punteggio presentazione: "))

        if i==0:
            dizionario[nominativo].append(("antipasti", (creativita, gusto, presentazione), categoriaChef))
        if i==1:
            dizionario[nominativo].append(("primi", (creativita, gusto, presentazione), categoriaChef))
        if i==2:
            dizionario[nominativo].append(("secondi", (creativita, gusto, presentazione), categoriaChef))
        if i==3:
            dizionario[nominativo].append(("dessert", (creativita, gusto, presentazione), categoriaChef))
        if i==4:
            dizionario[nominativo].append(("piatti unici", (creativita, gusto, presentazione), categoriaChef))


while True:
    print("n1.Aggiunta categoria piatto \n2.Stampa chef \n3.Stampa dati piatto \n4.Punteggio totale massimo e media punteggi totali \n5.Aggiunta chef nuovo")
    scelta=int(input("scelta: "))
    if scelta==1:
        nuovaCategoria()
    elif scelta==2:
        nomeChef=input("Inserisci il nome dello chef: ")
        stampaChef(nomeChef)
    elif scelta==3:
        tipoPiattoInserito=input("Inserisci la categoria piatto: ")
        datiPiatto(tipoPiattoInserito)
    elif scelta==4:
        categoriaPiattoInserito=input("Inserisci la categoria piatto: ")
        categoriaChefInserito=input("Inserisci la categoria dello chef: ")
        totaleMassimo(dizionario, categoriaPiattoInserito, categoriaChefInserito)
        media(dizionario, categoriaPiattoInserito, categoriaChefInserito)
    elif scelta==0:
        break