from Imputato import Imputato
from AssegnaPena import AssegnaPena
from AssegnaDurata import AssegnaDurataReclusione
from AssegnaTipoCarcere import AssegnaTipoCarcere
from VisualizzaCarceri import VisualizzaCarceri

if __name__ == '__main__':
    imputato = Imputato
    predizionepena = AssegnaPena
    predizionedurata = AssegnaDurataReclusione
    predizionetipocarcere = AssegnaTipoCarcere
    carceri = VisualizzaCarceri
    print(" ----------------------------------------------------------------------------------\n")
    print("                                  SIMULATORE GIUDICE                               \n")
    print(" ----------------------------------------------------------------------------------\n\n")
    nome = input(f"Inserisci il nome dell'imputato: ")
    cognome = input(f"Inserisci il cognome dell'imputato: ")
    print("Inserisci il reato dell'imputato:\n 1 = Omicidio\n"
          " 2 = Furto d'auto\n 3 = Furto abitazione\n 4 = Furto banca/posta\n 5 = Spaccio/Droga\n "
          "6 = Complice in un reato\n 7 = Violenza/Stupro\n 8 = Truffa\n 9 = Usura ")
    reato = int(input("Inserisci il numero corrispondente al reato: "))

    while(reato < 1) or (reato > 9):
        reato = int(input("Il numero corrsipondente al reato non e' valido reinserirlo: "))

    eta = int(input("Inserisci l'eta dell'imputato: "))
    precedenti = int(input("Inserisci il numero di precedenti penali dell'imputato (da 0 a 4): "))

    while(precedenti < 0) or (precedenti > 4):
        precedenti = int(input("Il numero corrsipondente ai precedenti penali non e' valido reinserirlo: "))

    imputato.inserimento_nome(nome)
    imputato.inserimento_cognome(cognome)
    imputato.inserimento_reato(reato)
    imputato.inserimento_eta(eta)
    imputato.inserimento_precedentipenali(precedenti)
    pena = predizionepena.predizione_pena(imputato)
    imputato.inserimento_pena(pena)
    if pena == 1:
        print(f"Tipologia pena: Ergastolo")
    elif pena == 2:
        print(f"Tipologia pena: Carcere")
    elif pena == 3:
        print(f"Tipologia pena: Arresti domiciliari")

    if pena != 1:
        durata = predizionedurata.predizione_durata(imputato)
        imputato.inserimento_durata(durata)
        if pena == 2:
            print(f"Anni di reclusione in carcere: {imputato.restituisci_durata()}")
        else:
            print(f"Mesi di condanna agli arresti domiciliari: {imputato.restituisci_durata()}")

    tipocarcere = predizionetipocarcere.predizione_tipocarcere(imputato)
    imputato.inserimento_tipologiacarcere(tipocarcere)
    if pena != 3:
        if tipocarcere == 1:
            print("L'imputato e' stato assegnato all'istituto penitenziario minorile.")
        elif tipocarcere == 2:
            print("L'imputato e' stato assegnato all'istituto penitenziario.")
        elif tipocarcere == 3:
            print("L'imputato e' stato assegnato all'istituto penitenziario di massima sicurezza.")
        carceri.visualizza_carceri(tipocarcere)
    else:
        print("L'imputato scontera' la pena nella sua abitazione o in centri appositi.")

    print(" ----------------------------------------------------------------------------------\n")
    print("                          L'IMPUTATO E' DICHIARATO COLPEVOLE!                      \n")
    print(" ----------------------------------------------------------------------------------\n\n")

pass
