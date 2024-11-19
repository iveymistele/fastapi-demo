#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd 
import json
import os

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/genres')
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        return {"Error": "MySQL Error: " + str(e)}

@app.get("/songs")
def get_songs():
    query = "SELECT songs.title, songs.album, songs.artist, songs.year, songs.file, songs.image, genres.genre FROM songs JOIN genres ON songs.genre = genres.genreid;"
    try:
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        return {"Error": "MySQL Error: " + str(e)}


@app.get("/")  # zone apex
def zone_apex():
    return {"Welcome to ": "my app"}

## @app.get("/customer/{idx}")
## def customer(idx : int):
   # read the data into a df 
  ## df = pd.read_csv("../customers.csv")
   # filter the data based on interest
  ## customer = df.iloc[idx]
  ## return customer.to_dict()

@app.post("/get_body")
def get_body(request: Request):
   return request.json()

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "zyh4up"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()
