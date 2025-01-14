from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {"request": request, "title": "Page pricipale"}
    return templates.TemplateResponse("index.html", context)

@app.get("/chatbot/", response_class=HTMLResponse)
async def chatbot(request: Request):
    context = {"request": request, "title": "Chatbot"}
    return templates.TemplateResponse("chatbot.html", context)


@app.get("/recherche/", response_class=HTMLResponse)
async def recherche(request: Request):
    context = {"request": request, "title": "Recherche dans un document"}
    return templates.TemplateResponse("recherche.html", context)