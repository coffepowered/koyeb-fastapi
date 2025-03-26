from fasthtml.common import Div, P, FastHTML
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "Hello World from main app"}

'''
subapi = FastAPI()
@subapi.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}
'''


app2 = FastHTML()
@app2.get('/x')
def get(): return Div(P('Hello World!'), hx_get="/change")

app.mount("/subapi", app2)