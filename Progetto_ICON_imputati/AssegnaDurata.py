import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error
import seaborn as snp
import matplotlib.pyplot as plt
#from sklearn.ensemble import AdaBoostRegressor
#from sklearn.tree import DecisionTreeRegressor
#from sklearn.ensemble import BaggingRegressor
#from sklearn.utils import check_random_state


class AssegnaDurataReclusione:
    imputati = pd.read_csv("Dataset_imputati.csv", delimiter=";")
    modello = RandomForestRegressor(n_estimators=100)
    #DTR=DecisionTreeRegressor(max_depth=1)
    #modello = AdaBoostRegressor(n_estimators=50, base_estimator=DTR ,learning_rate=1)
    #rng = check_random_state(0)
    #modello = BaggingRegressor(base_estimator=DecisionTreeRegressor(), max_samples=1.0, bootstrap=True, random_state=0)

    @classmethod
    def predizione_durata(cls, imputato):
        y = cls.imputati["durata"]
        x = cls.imputati[["reato", "pena", "precedenti_penali"]]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        cls.modello.fit(x_train, y_train)
        datipredizione = pd.DataFrame(data={"reato": [imputato.restituisci_reato()],
                                            "pena": [imputato.restituisci_pena()],
                                            "precedenti_penali": [imputato.restituisci_precedentipenali()]})
        durata = int(cls.modello.predict(datipredizione))
        k = 10
        kf = KFold(n_splits=k, shuffle=True)
        result = cross_val_score(cls.modello, x, y, cv=kf)
        #print(result)
        print(f"Accuratezza media predizione durata pena: {format(result.mean())}")
        p_train = cls.modello.predict(x_train) #p_train contiene le predizioni(y) sui dati x di training
        p_test = cls.modello.predict(x_test) #p_test contiene le predizioni(y) sui dati x di test
        #calcolo errori
        mae_train = mean_absolute_error(y_train, p_train)
        mae_test = mean_absolute_error(y_test, p_test)

        print('MAE test', mae_test)
        print('MAE train', mae_train)
        res = y_test-p_test
        snp.scatterplot(x=y_test, y=res)
        plt.show()
        return durata
