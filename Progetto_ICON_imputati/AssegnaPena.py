import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


class AssegnaPena:
    imputati = pd.read_csv("Dataset_imputati.csv", delimiter=";")
    modello = KNeighborsClassifier(5)

    @classmethod
    def predizione_pena(cls, imputato):
        y = cls.imputati.pena
        x = cls.imputati[["reato", "eta", "precedenti_penali"]]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
        cls.modello.fit(x_train, y_train)
        datipredizione = pd.DataFrame(data={"reato": [imputato.restituisci_reato()],
                                            "eta": [imputato.restituisci_eta()],
                                            "precedenti_penali": [imputato.restituisci_precedentipenali()]})
        pena = cls.modello.predict(datipredizione)
        k = 10
        kf = KFold(n_splits=k, random_state=None)
        result = cross_val_score(cls.modello, x, y, cv=kf)
        accuratezza = float(format(result.mean()))
        print("Accuratezza media predizione assegnazione pena: %.2f" % accuratezza)
        return int(pena)
