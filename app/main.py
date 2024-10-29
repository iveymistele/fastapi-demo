#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hi ": "Bye"}

@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@app.get("/square/{e}")
def square(e: int):
   return {"square": e * e}

@app.get("/reverse_str/{text}")
def reverse_str(text: str):
   return {"reversed": text[::-1]}


@app.get("/is_prime/{f}")
def is_prime(f: int):
   if f <= 1:
     return {"is_prime": False}
   for i in range(2, int(f ** 0.5) + 1):
     if f % i == 0:
         return {"is_prime": False}
   return {"is_prime": True}

@app.get("/char_count/{word}")
def char_count(word: str):
    return {"char_count": len(word)}

@app.get("/uppercase/{text}")
def uppercase(text: str):
   return {"uppercase": text.upper()}

@app.get("/subtract/{a}/{b}")
def subtract(a: int, b: int):
   return {"subtract": a-b}


