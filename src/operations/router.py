from fastapi import APIRouter, Depends

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import order
from src.operations.schemas import OrderCreate


router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.get("/spec")
async def get_specific_orders(customer_name: int, session: AsyncSession = Depends(get_async_session)):
    query = select(order).where(order.c.owner_id == customer_name)
    result = await session.execute(query)
    return result.all()

@router.get("/")
async def get_all_orders(session: AsyncSession = Depends(get_async_session)):
    query = select(order)
    result = await session.execute(query)
    return result


@router.post("/")
async def add_orders(new_order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order).values(**new_order.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.post("/up")
async def update_order_status(new_status: str, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order.c.status).values(new_status)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}