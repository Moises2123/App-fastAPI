from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app_moico.crud import create_user, get_user, get_all_users, delete_user
from app_moico.esquema import UserCreate, UserResponse
from app_moico.basededato import get_session

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user_route(user: UserCreate, db: AsyncSession = Depends(get_session)):
    return await create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_route(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserResponse])
async def get_all_users_route(db: AsyncSession = Depends(get_session)):
    return await get_all_users(db)

@router.delete("/{user_id}", status_code=204)
async def delete_user_route(user_id: int, db: AsyncSession = Depends(get_session)):
    success = await delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
