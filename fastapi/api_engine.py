from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from scripts.numerical_outlier_detector import DataModelNum
from scripts.categorical_outlier_detector import DataModelCat
import sklearn
import numpy as np
import pandas

app = FastAPI()

# read csvs from /data
# transfer to dataframe and array

data_num = pandas.read_csv('data/dane_numeryczne.csv')
data_cat = pandas.read_csv('data/dane_kategoryczne.csv')

print(data_num)
print(data_cat)

df_training_num = np.array(data_num)
data_num = DataModelNum(df_training_num)

df_training_cat = np.array(data_cat)
data_cat = DataModelCat(df_training_cat)

class RequestBody(BaseModel):
    plec: Optional[int] = 0
    stan_cywilny: Optional[int] = 0
    wyksztalcenie: Optional[int] = 0
    kategoria: Optional[str] = ""
    kwota_obciazenia: Optional[float] = 0
    miesiac_operacji: Optional[int] = 0
    wiek_klienta: Optional[int] = 0
    wiek_konta: Optional[int] = 0

@app.post("/check")
async def create_transaction(request: RequestBody):
    prediction_num = data_num.is_outlier(np.array([request.kwota_obciazenia, request.miesiac_operacji, request.wiek_klienta, request.wiek_konta]))
    prediction_cat = data_kat.is_outlier(np.array([request.plec, request.stan_cywilny, request.wyksztalcenie, request.kategoria]))
    return {'prediction_num': prediction_num, 'prediction_cat': prediction_cat}
