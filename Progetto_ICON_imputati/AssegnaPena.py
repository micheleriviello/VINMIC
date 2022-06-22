import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from numpy import mean
from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
import scikitplot as skplt
import matplotlib.pyplot as plt

class AssegnaPena:
    imputati = pd.read_csv("Dataset_imputati.csv", delimiter=";")
    #modello = KNeighborsClassifier(5)
    #modello = DecisionTreeClassifier()
    #modello = MLPClassifier()
    modello = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
    #modello = GaussianNB()

    @classmethod
    def predizione_pena(cls, imputato):
        y = cls.imputati.pena
        x = cls.imputati[["reato", "eta", "precedenti_penali"]]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
        cls.modello.fit(x_train, y_train)
        datipredizione = pd.DataFrame(data={"reato": [imputato.restituisci_reato()],
                                            "eta": [imputato.restituisci_eta()],
                                            "precedenti_penali": [imputato.restituisci_precedentipenali()]})
        pena = cls.modello.predict(datipredizione)
        k = 10
        kf = KFold(n_splits=k, shuffle=True)
        result = cross_val_score(cls.modello, x, y, cv=kf, n_jobs=-1)
        #print(result)
        accuratezza = mean(result)
        print("Accuratezza media predizione assegnazione pena: %.2f" % accuratezza)
        p_test = cls.modello.predict(x_test)
        report=classification_report(p_test, y_test)
        print(report)
        skplt.metrics.plot_confusion_matrix(p_test,y_test)
        plt.show()
        return int(pena)
