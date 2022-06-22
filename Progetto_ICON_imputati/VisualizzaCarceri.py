import pytholog as pl


class VisualizzaCarceri:

    @classmethod
    def visualizza_carceri(cls, tipocarcere):
        parametro_scelta = 0
        tipo = ""
        if tipocarcere == 1:
            tipo = "minorile"
        elif tipocarcere == 2:
            tipo = "penitenziario"
        elif tipocarcere == 3:
            tipo = "massima_sicurezza"
        while parametro_scelta != 4:
            kb = pl.KnowledgeBase("carceri")
            kb.from_file("kb_carceri.pl")
            print(f"Data la tipologia di carcere che in questo caso e' : {tipo} "
                  f", in base a quale parametro vuole cercare le carceri italiane? Premere:")
            print("1 per cercare tramite la citta")
            print("2 per cercare tramite la regione")
            print("3 per cercare tramite i posti disponibili")
            print("premere 4 per uscire!")
            parametro_scelta = int(input("Inserisci il numero corrispondente alla "
                                         "tipologia di ricerca che si vuole effettuare:"))
            while (parametro_scelta < 1) or (parametro_scelta > 4):
                parametro_scelta = int(input("Numero non valido, reinserirlo:"))
            if parametro_scelta == 1:
                citta = input("Inserire la citta' in cui vorresti verificare se ci sia un carcere: ").lower()
                print("Ecco le carceri trovate:")
                listacarceri = list(kb.query(pl.Expr("cercacarcere("+tipo+", "+citta+", Regione, Posti)")))
                for carceri in listacarceri:
                    print(carceri)
            elif parametro_scelta == 2:
                regione = input("Inserisci la regione in cui vorresti verificare se ci fossero carceri: ").lower()
                print("Ecco le carceri trovate:")
                listacarceri = list(kb.query(pl.Expr("cercacarcere("+tipo+", Citta, "+regione+", Posti)")))
                for carceri in listacarceri:
                    print(carceri)
            elif parametro_scelta == 3:
                nposti = str(input("Inserisci il numero di posti delle carceri da ricercare: "))
                print("Ecco le carceri trovate:")
                listacarceri = list(kb.query(pl.Expr("cercacarcere("+tipo+", Citta, Regione, "+nposti+")")))
                for carceri in listacarceri:
                    print(carceri)
