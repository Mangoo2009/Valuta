import uvicorn
from fastapi import FastAPI, Form, Depends, Request, HTTPException
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
def main(request: Request):
    return templates.TemplateResponse(request, 'main.html')

@app.get('/{id}')
def get_valuta(request: Request, id: str):
    return templates.TemplateResponse(request, 'valute.html', {'id': id.upper()})

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
