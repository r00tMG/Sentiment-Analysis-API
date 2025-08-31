from fastapi import APIRouter, Request, Form, status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
router = APIRouter(
    tags=["predictions"]
)
templates = Jinja2Templates(directory="templates")
@router.post("/predict")
async def prediction(
        request:Request,
        texte:str=Form(...)
    ):
    errors = []
    if not texte:
        errors.append({"texte":"Un texte est requis"})
    if errors:
        return templates.TemplateResponse("/index.html", {
            "request": request,
            "errors":errors
        })
    response = classifier(texte)
    request.session['response'] = response
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)