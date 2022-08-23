import pathlib
from pipes import Template
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
BASE_DIR = pathlib.Path(__file__).parent
print((BASE_DIR / 'templates').exists())
app = FastAPI()
Templates = Jinja2Templates(directory=str(BASE_DIR / '/templates'))

@app.get("/",response_class=HTMLResponse)

def home_view(request: Request):
    return '<h1>helloworld</h1>'

@app.post("/")

def home_detail_view():
    return {'hello': 'worldview'}
