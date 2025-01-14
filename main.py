from fastapi import FastAPI, Request, File, UploadFile
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


# uploaded_content = ""

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    uploaded_content = ""
    # global uploaded_content
    uploaded_content = (await file.read()).decode("utf-8")
    return {"filename": file.filename, "content": uploaded_content}


# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     try:
#         uploaded_content = await file.read()
#         return {"filename": file.filename, "content": uploaded_content.decode("utf-8")}
#     except Exception as e:
#         return {"error": str(e)}