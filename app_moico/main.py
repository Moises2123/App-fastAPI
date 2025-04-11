from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app_moico.routes import router
import os

app = FastAPI(title="FastAPI CRUD Example")

# Incluir las rutas definidas en `routes.py`
app.include_router(router, prefix="/users", tags=["Users"])

# Configurar la ruta para servir archivos estáticos
current_directory = os.path.dirname(os.path.abspath(__file__))  # Obtener la ruta del archivo actual
static_directory = os.path.join(current_directory, "../static")  # Ir un nivel arriba y luego a la carpeta `static`
app.mount("/static", StaticFiles(directory=static_directory), name="static")

@app.get("/")
async def root():
    return {"message": "BIENVENIDO A MI EJEMPLO DE fastAPI realizado por Moises Vasquez!"}
