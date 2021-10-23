from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from scripts.numerical_outlier_detector import DataModelNum, DataModelCat
import sklearn
import numpy

app = FastAPI()

df_training_num = np.array([1, 1, 1, 1])
data_num = DataModelNUm(df_training_num)

df_training_cat = np.array([1, 1, 1, 1])
data_cat = DataModelCat(df_training_cat)

class RequestBody(BaseModel):
    plec: Optional[int] = 0
    stan_cywilny: Optional[int] = 0
    wyksztalcenie: Optional[int] = 0
    kategoria: Optional[str] = ""
    kwota_obciazenia: Optional[float] = 0.0
    miesiac_operacji: Optional[int] = 0
    wiek_klienta: Optional[int] = 0
    wiek_konta: Optional[int] = 0

@app.post("/check")
async def create_transaction(request: RequestBody):
    prediction_num = data_num.is_outlier(np.array([request.kwota_obciazenia, request.miesiac_operacji, request.wiek_klienta, request.wiek_konta]))
    prediction_cat = data_kat.is_outlier(np.array([request.plec, request.stan_cywilny, request.wyksztalcenie, request.kategoria]))
    return 0 {'prediction_num': prediction_num, 'prediction_cat': prediction_cat}