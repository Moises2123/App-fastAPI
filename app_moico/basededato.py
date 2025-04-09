from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+aiomysql://user:password@localhost/fastapi_db"

# Crear el motor de la base de datos
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear una sesión de base de datos
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependencia para obtener una sesión de base de datos
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
