tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

def media_gol_partite(tupla_partite):
    punteggi=[]
    num=0
    for squadraCasa, squadraOspite, pCasa, pOspiti in tupla_partite:
        golPartita= pCasa + pOspiti
        punteggi.append(golPartita)
        num+=1
    media= round((sum(punteggi))/num,2)
    return media

def media_gol_squadra(tupla_partite, squadra):
    pSquadra=[]
    num=0
    for squadraCasa, squadraOspite, pCasa, pOspiti in tupla_partite:
        if(squadra==squadraCasa):
            pSquadra.append(pCasa)
            num+=1
        elif(squadra==squadraOspite):
            pSquadra.append(pOspiti)
            num+=1
    mediaSquadra=round(sum(pSquadra)/num,2)
    return mediaSquadra

def partita_con_piu_gol(tupla_partite):
    gol=[]
    partite=[]
    for squadraCasa, squadraOspite, pCasa, pOspiti in tupla_partite:
        golPartita= pCasa + pOspiti
        gol.append(golPartita)
  
    for squadraCasa, squadraOspite, pCasa, pOspiti in tupla_partite:
        golPartita= pCasa + pOspiti
        if(golPartita==max(gol)):
            partita= squadraCasa, squadraOspite, pCasa, pOspiti
            partite.append(partita)
    return partite

def partita_con_meno_gol(tupla_partite):
    gol=[]
    partite=[]
    for squadraCasa, squadraOspite, pCasa, pOspiti in tupla_partite:
        golPartita= pCasa + pOspiti
        gol.append(golPartita)

    for squadraCasa, squadraOspite, pCasa, pOspiti in tupla_partite:
        golPartita= pCasa + pOspiti
        if(golPartita==min(gol)):
            partita= squadraCasa, squadraOspite, pCasa, pOspiti
            partite.append(partita)
    return partite
'''
def percentuale_vittorie_squadra(tupla_partite, squadra):
    numPartite=0
    partiteVinte=0
    for tupla in tupla_partite:
        numPartite+=1
    for squadraCasa, squadraOspite, pCasa, pOspiti in tupla_partite:
        if(squadra==squadraCasa):
            if(pCasa>pOspiti):
                partiteVinte+=1
        elif(squadra==squadraOspite):
            if(pCasa<pOspiti):
                partiteVinte+=1
    percentuale= (numPartite/partiteVinte)*100
    return percentuale
'''


print("1.media_gol_partite \n2.media_gol_squadra \n3.partita_con_piu_gol \n4.partita_con_meno_gol \n5.percentuale_vittorie_squadra")
while True:
    scelta=int(input("Inserisci la scelta: "))
    if scelta==1:
        print(f"Media gol in tutte le partite: {media_gol_partite(tupla_partite):}")
        break
    elif scelta==2:
        while True:
            squadraTrovata= False
            squadra=input("Inserisci una squadra: ")
            for squadraCasa, squadraOspite, pCasa, pOspiti in tupla_partite:
                if(squadra==squadraCasa or squadra==squadraOspite):
                    squadraTrovata= True
            if squadraTrovata == True:
                break
        print(f"Media gol di {squadra}: {media_gol_squadra(tupla_partite, squadra)}")
        break
    elif scelta==3:

        print(f"Tupla con la partita con i gol piu alti: {partita_con_piu_gol(tupla_partite)}")
        break
    elif scelta==4:
        print(f"Tupla con la partita con i gol piu bassi: {partita_con_meno_gol(tupla_partite)}")
        break
    else:
        print("Scelta non valida")


