from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/user")
def read_root():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    json_data = response.json()
    return json_data

@app.get("/")
def inicio():
    return {'mensaje':'Esta en el inicio '}