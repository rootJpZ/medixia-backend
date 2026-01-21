from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="MEDIXIA")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class LoginData(BaseModel):
    username: str
    password: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "MEDIXIA"}

@app.post("/login")
def login(data: LoginData):
    if data.username == "julianPZ" and data.password == "150635Jp":
        return {"token": "medixia-token"}

    raise HTTPException(
        status_code=401,
        detail="Credenciales incorrectas"
    )

@app.get("/medicamentos")
def medicamentos():
    return [{
        "principio_activo_anmat": "METFORMINA",
        "marca": "Glucophage",
        "presentacion": "850 mg",
        "laboratorio": "Merck",
        "obra_social": "PAMI",
        "cobertura": "100%"
    }]
