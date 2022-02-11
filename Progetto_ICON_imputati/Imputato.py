class Imputato:
    nome = ""
    cognome = ""
    reato = 0
    precedenti = 0
    eta = 0
    pena = 0
    tipocarcere = 0
    durata = 0

    @classmethod
    def restituisci_nome(cls):
        return cls.nome

    @classmethod
    def restituisci_durata(cls):
        return cls.durata

    @classmethod
    def restituisci_cognome(cls):
        return cls.cognome

    @classmethod
    def restituisci_reato(cls):
        return cls.reato

    @classmethod
    def restituisci_eta(cls):
        return cls.eta

    @classmethod
    def restituisci_pena(cls):
        return cls.pena

    @classmethod
    def restituisci_tipologiacarcere(cls):
        return cls.tipocarcere

    @classmethod
    def restituisci_precedentipenali(cls):
        return cls.precedenti

    @classmethod
    def inserimento_nome(cls, nome):
        cls.nome = nome

    @classmethod
    def inserimento_durata(cls, durata):
        cls.durata = durata

    @classmethod
    def inserimento_cognome(cls, cognome):
        cls.cognome = cognome

    @classmethod
    def inserimento_reato(cls, reato):
        cls.reato = reato

    @classmethod
    def inserimento_eta(cls, eta):
        cls.eta = eta

    @classmethod
    def inserimento_pena(cls, pena):
        cls.pena = pena

    @classmethod
    def inserimento_tipologiacarcere(cls, tipocarcere):
        cls.tipocarcere = tipocarcere

    @classmethod
    def inserimento_precedentipenali(cls, precedenti):
        cls.precedenti = precedenti
