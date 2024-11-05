dati=[
    ("Milano", [("gennaio", "N/D"),("febbraio", 23), ("marzo", 30),("febbraio", 14),
                ("aprile", 21),("maggio", 11),("giugno", 17),
                ("luglio", 11),("agosto", 13),("settembre", 30),
                ("otoobre", 26),("novembre", "N/D"),("dicembre", 27),]),
    ("Monza", [("gennaio", 12),("febbraio", 23), ("marzo", 14),("febbraio", "N/D"),
                ("aprile", 21),("maggio", "N/D"),("giugno", 17),
                ("luglio", 11),("agosto", 13),("settembre", 30),
                ("otoobre", 26),("novembre", 12),("dicembre", 27),])
]

def analizza(cittaInserita):
    somma=0
    num=0
    for nome, mesi  in dati:
        if(cittaInserita==nome):
            for mese, pioggia in mesi:
                if(pioggia!="N/D"):
                    num+=1
                    somma+=pioggia
    media=round(somma/num,2)

    valoreMax=0
    valoreMin=1000
    mesiMax=[]
    mesiMin=[]

#max
    for nome, mesi  in dati:
        if(cittaInserita==nome):
            for mese, pioggia in mesi:
                 if(pioggia!="N/D"):
                    if(pioggia>valoreMax):
                        valoreMax=pioggia
            for mese, pioggia in mesi:
                if(pioggia!="N/D"):
                    if(pioggia==valoreMax):
                        mesiMax.append(mese)

#min
    for nome, mesi  in dati:
        if(cittaInserita==nome):
            for mese, pioggia in mesi:
                if(pioggia!="N/D"):
                    if(pioggia<valoreMin):
                        valoreMin=pioggia
            for mese, pioggia in mesi:
                if(pioggia!="N/D"):
                    if(pioggia==valoreMin):
                        mesiMin.append(mese)

    
    if(num>0):
        return (media,(valoreMax, mesiMax), (valoreMin, mesiMin))
    else:
        return "Tupla vuota"


#richiamo la funzione
while True:
    cittaInserita=input("Inserisci la citta: ")
    cittaTrovata=False
    for nome, mesi  in dati:
        if(nome in cittaInserita):
            cittaTrovata=True
    if(cittaTrovata==True):
        break

(media,(valoreMax, mesiMax), (valoreMin, mesiMin))= analizza(cittaInserita)
print(analizza(cittaInserita))