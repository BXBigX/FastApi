from fastapi import FastAPI

app = FastAPI()


@app.get("/Sum/{a}/{b}")
def calculated_plus(a: int, b: int):
    return {"Sum ==": a+b}


@app.get("/Difference/{a}/{b}")
def calculated_minus(a: int, b: int):
    return {"Difference ==": a-b}


@app.get("/Division/{a}/{b}")
def calculated_division(a: int, b: int):
    return {"Division ==": a/b}


@app.get("/Multiplication/{a}/{b}")
def calculated_multiplication(a: int, b: int):
    return {"Multiplication ==": a*b}
