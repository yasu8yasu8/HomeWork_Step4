from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    number: int


@app.post("/pikachu")
def pikachu(item: Item):
    if item.number <=0:
        raise HTTPException(status_code=400, detail="ピカピー！！")
    return {"result": "ピカ" * (item.number - 1) + "、ピカチュウ！"}