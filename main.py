from fastapi import FastAPI, Request



app = FastAPI()



@app.get("/")
async def read_root():
    context = {"title": "Welcome to FastAPI"}
    return 'oussama 50'