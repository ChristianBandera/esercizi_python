tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("marzo", ("gas", 120)),
        ("gennaio", ("gas", 150)),
        ("aprile", ("elettrico", 350)),
        ("giugno", ("gas", 130)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("gas", 130)),
        ("gennaio", ("gas", 150)),
        ("aprile", ("elettrico", 370)),
        ("giugno", ("gas", 120)),
    ]),
    ("Roma", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("gas", 130)),
        ("gennaio", ("gas", 150)),
        ("aprile", ("elettrico", 370)),
        ("giugno", ("gas", 120)),
    ])
)

def analizza_consumi_energetici(cittaInserita, consumoInserito):
    sommaRisorsa=0
    numRisorsa=0
    soldiMax=[]
    mese_max_risorsa=[]
    for citta, dati in tupla_consumi_energetici:
        for (mese,(consumo, soldi)) in dati:
            if(consumoInserito== consumo and cittaInserita== citta):
                sommaRisorsa+=soldi
                numRisorsa+=1
    media_risorsa=round(sommaRisorsa/numRisorsa,2)

    for citta, dati in tupla_consumi_energetici:
        for (mese,(consumo, soldi)) in dati:
            if(consumoInserito== consumo and cittaInserita== citta):
                soldiMax.append(soldi)
    max_risorsa= max(soldiMax)

    for citta, dati in tupla_consumi_energetici:
        for (mese,(consumo, soldi)) in dati:
            if(consumoInserito== consumo and cittaInserita== citta):
                if(soldi==max_risorsa):
                    mese_max_risorsa.append(mese)
    return(media_risorsa, (max_risorsa, mese_max_risorsa))

while True:
    cittaTrovata=False
    consumoTrovato=False
    cittaInserita= input("Inserisci una citta: ")
    consumoInserito= input("Inserisci un consumo: ")
    for citta, dati in tupla_consumi_energetici:
        for (mese,(consumo, soldi)) in dati:
            if(citta==cittaInserita and consumo== consumoInserito):
                cittaTrovata=True
                consumoTrovato=True
    if(cittaTrovata==True and consumoTrovato==True):
        break

risultato_analisi = analizza_consumi_energetici(cittaInserita, consumoInserito)
print(risultato_analisi)
    