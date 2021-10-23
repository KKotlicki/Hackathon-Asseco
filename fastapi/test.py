from scripts.numerical_outlier_detector import DataModelNum
import pandas as pd
import numpy as np

df_training = pd.read_csv('data/dane_numeryczne.csv')
arr_training = np.array(df_training)
arr_training = np.delete(arr_training, 0, 1)
model = DataModelNum(arr_training)
record1 = np.array([[30000, 11, 48, 149]])
print(f"Kwota wypłaty: 30 000\nMiesiąc: 11\nWiek klienta: 48\nCzas aktywności konta: 149\n\n\nCzy jest anomalią:")
print(model.is_outlier(record1))
print("\nIlość znalezionych anomalii w danych treningowych: ")
print(f"{model.outliers_rate * 100}%")
