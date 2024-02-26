from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# templates object for re-use
templates = Jinja2Templates(directory="../templates")
# home app

@app.get('/', response_class=HTMLResponse)
def home_template(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")

# auth app


@app.get("/auth", response_class=HTMLResponse)
def auth_template(request: Request):
    return templates.TemplateResponse(request=request, name="auth.html")

# Library app

@app.get("/library")
def library_template(request: Request):
    return templates.TemplateResponse(request=request, name="library.html")
    