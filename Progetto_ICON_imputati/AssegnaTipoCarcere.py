import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


class AssegnaTipoCarcere:
    imputati = pd.read_csv("Dataset_imputati.csv", delimiter=";")
    modello = DecisionTreeClassifier()

    @classmethod
    def predizione_tipocarcere(cls, imputato):
        np.random.seed(0)
        y = cls.imputati["tipo_carcere"]
        x = cls.imputati[["reato", "pena", "eta"]]
        cls.modello.fit(x, y)
        datipredizione = pd.DataFrame(data={"reato": [imputato.restituisci_reato()],
                                            "pena": [imputato.restituisci_pena()],
                                            "eta": [imputato.restituisci_eta()]})
        tipocarcere = cls.modello.predict(datipredizione)
        k = 10
        kf = KFold(n_splits=k, random_state=None)
        result = cross_val_score(cls.modello, x, y, cv=kf)
        print(f"Accuratezza media predizione luogo in cui scontare la pena: {format(result.mean())}")
        return int(tipocarcere)
