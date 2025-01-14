from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import re

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




@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
        
        file_content = await file.read()
        uploaded_content = file_content.decode("utf-8")  # قراءة الملف كنص
        doc_phrases = stocker_liste(uploaded_content)  # تقسيم النص إلى جمل
        numbered_phrases = [{"number": idx + 1, "sentence": phrase} for idx, phrase in enumerate(doc_phrases)]
        return {"filename": file.filename, "content": numbered_phrases}







# ------------------------------------------------------------- Fonction ---------------------
def stocker_liste(corpus):
    phrases = re.split(r'[.?!]\s*', corpus.strip())  # Séparation avec . ? ou !
    phrases = [phrase for phrase in phrases if phrase]  # Filtrer les phrases vides
    return phrases