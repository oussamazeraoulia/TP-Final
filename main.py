from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {"request": request, "title": "Page pricipale"}
    return templates.TemplateResponse("index.html", context)

@app.get("/chatbot/")
async def chatbot(request: Request):
    context = {"request": request, "title": "Chatbot"}
    file_path = os.path.join("templates", "chatbot.html")
    # return templates.TemplateResponse("chatbot.html", context)
    return HTMLResponse(open(file_path).read())


@app.get("/recherche/", response_class=HTMLResponse)
async def recherche(request: Request):
    context = {"request": request, "title": "Recherche dans un document"}
    return templates.TemplateResponse("recherche.html", context)


uploaded_content = ""

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    global uploaded_content
    uploaded_content = (await file.read()).decode("utf-8")
    return {"filename": file.filename, "content": uploaded_content}