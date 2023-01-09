from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware

import pickle
import os
from typing import Optional
from pydantic import BaseModel
import numpy as np

app = FastAPI()

# @app.middleware("http")
# async def add_cors_headers(request: Request, response: Response):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Methods"] = "POST, GET"
#     response.headers["Access-Control-Allow-Headers"] = "Content-Type, Accept, OPTIONS"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pickle_in=open("kaggle_titanic_model.pkl","rb")
pred=pickle.load(pickle_in)

class Passenger(BaseModel):
    Pclass: Optional[int]
    Sex: Optional[int]
    Age: Optional[float]
    SibSp: Optional[int]
    eParch: Optional[int]

@app.get("/")
def root():
    return {"message": "Api Titanic"}

@app.post(path="/predict")

def predict(data:Passenger):
    data=data.dict()
    Pclass=data["Pclass"] 
    Age= data["Age"] 
    Sex= data["Sex"] 
    SibSp= data["SibSp"] 
    eParch= data["eParch"]
    #x_test=[3,0,0.28947368,1,1]
    #max_age=80
    x_test=[Pclass,Age/80,Sex,SibSp,eParch]
    x_test=np.reshape(x_test,(1,5))
    prediction = pred.predict(x_test)
    print("Prediccion: ",prediction) 
    if(int(prediction[0])>0.5):
        prediction="Survived"
        print("Survived")
    else:
        prediction="Do not Survived"
        print("Do not Survived")

    return {
        'prediction': prediction
    }