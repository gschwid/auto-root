from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/song/{name}")
def read_name(name: str):
    return {"Name": name}