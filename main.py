from typing import Union, Dict

import uvicorn
from fastapi import FastAPI, Request
from OPENAI.OPENAI_PRUEBA.openai_conect import Document, inference

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
#METODO PARA CALCULAR EL FACTORIAL
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@app.get("/factorial/{number}")
def calculate_factorial(number: int):
    result = factorial(number)
    return {"number": number, "factorial": result}


@app.post('/inference', status_code=200)
def inference_endpoint(request: Request, response: Dict[str, str]):
    doc = Document(prompt=request.body().decode('utf-8'))  # Obtiene el prompt del cuerpo de la solicitud
    response = inference(doc.prompt)
    return {
        'inference': response[0],
        'usage': response[1]
    }

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1", port=9033)