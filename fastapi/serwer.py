from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

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
    return 0