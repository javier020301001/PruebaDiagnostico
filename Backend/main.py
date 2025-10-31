from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/posteos', tags=['mostrarposteos'])
def mostrarposteos():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    datos = response.json()
    datos = datos[:10]

    return datos






