import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


class AssegnaDurataReclusione:
    imputati = pd.read_csv("Dataset_imputati.csv", delimiter=";")
    modello = RandomForestRegressor(n_estimators=100)

    @classmethod
    def predizione_durata(cls, imputato):
        np.random.seed(0)
        y = cls.imputati["durata"]
        x = cls.imputati[["reato", "pena", "precedenti_penali"]]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        cls.modello.fit(x_train, y_train)
        datipredizione = pd.DataFrame(data={"reato": [imputato.restituisci_reato()],
                                            "pena": [imputato.restituisci_pena()],
                                            "precedenti_penali": [imputato.restituisci_precedentipenali()]})
        durata = int(cls.modello.predict(datipredizione))
        k = 10
        kf = KFold(n_splits=k, random_state=None)
        result = cross_val_score(cls.modello, x, y, cv=kf)
        print(f"Accuratezza media predizione durata pena: {format(result.mean())}")
        return durata
