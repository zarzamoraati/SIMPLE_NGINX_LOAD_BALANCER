from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home_server():
    return "Welcome Server 1"




