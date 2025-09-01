from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from router.huggingFace import classifier

router = APIRouter(
    tags=['home']
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("/index.html", {
        "request":request,
    })


