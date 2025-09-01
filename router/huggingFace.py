from fastapi import APIRouter, Request, Form, status, HTTPException
from starlette.templating import Jinja2Templates
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
router = APIRouter(
    tags=["predictions"]
)
templates = Jinja2Templates(directory="templates")
@router.post("/predict_form")
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
    if response:
        return templates.TemplateResponse("/index.html", {
            "request": request,
            "response":response,
            "texte":texte
        })

@router.post("/predict")
async def prediction(
        texte:str=Form(...)
    ):
    errors = []
    if not texte:
        errors.append({"texte":"Un texte est requis"})
    if errors:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errors[0].get('texte'))
    response = classifier(texte)
    if response:
        return response
