from fastapi import FastAPI, Request, File, UploadFile, HTTPException
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

# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     uploaded_content = ""
#     # global uploaded_content
#     uploaded_content = (await file.read()).decode("utf-8")
#     return {"filename": file.filename, "content": uploaded_content}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # الحد الأقصى لحجم الملف (مثلاً 5 ميجابايت)
    max_file_size = 5 * 1024 * 1024  # 5MB
    if file.size > max_file_size:
        raise HTTPException(status_code=413, detail="الملف كبير جدًا. الحد الأقصى هو 5 ميجابايت.")

    uploaded_content = ""
    try:
        uploaded_content = (await file.read()).decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"خطأ في قراءة الملف: {str(e)}")

    return {"filename": file.filename, "content": uploaded_content}