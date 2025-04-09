from fastapi import FastAPI
from app_moico.routes import router

app = FastAPI(title="FastAPI CRUD Example")

# Incluir las rutas definidas en `routes.py`
app.include_router(router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "BIENVENIDO A MI EJEMPLO DE fastAPI realizado por Moises Vasquez!"}
