from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.menu.models import menu
from src.menu.schemas import AddPosition, UpdatePosition

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)


@router.get("/")
async def get_menu(session: AsyncSession = Depends(get_async_session)):
    query = select(menu).where(menu.c.actuality == True)
    result = await session.execute(query)
    return result

@router.post("/")
async def add_position(new_position: AddPosition, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(menu).values(**new_position.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/update")
async def update_position(new_position: UpdatePosition, session: AsyncSession = Depends(get_async_session)):
    stmt = update(menu).where(menu.c.id == new_position.id).values(**new_position.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.post("/delete")
async def delete_position(position_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = update(menu).where(menu.c.id == position_id).values(actuality=False)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}