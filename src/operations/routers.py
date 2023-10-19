from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate, OperationUpdate

router = APIRouter(
    prefix="/operation",
    tags=["Operation"]
)


@router.get('/')
async def get_specific_operation(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "seccess",
            "data": result.mappings().all(),
            "details": None
        }
    except Exception as exc:
        return {
            "status": "error",
            "data": None,
            "details": exc
        }


@router.post('/')
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(operation).values(**new_operation.__dict__)
        await session.execute(stmt)
        await session.commit()
        return {"statue": HTTPException(status_code=201, detail="Operation added")}
    except Exception as exc:
        return {
            "status": "error",
            "data": None,
            "details": exc
        }


@router.delete('/operation_id')
async def delete_specific_operation(operation_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(operation).where(operation.c.id==operation_id)
        await session.execute(stmt)
        await session.commit()
        return {
            "status": HTTPException(status_code=404, detail="Operation deleted"),
        }
    except Exception as exc:
        return{
            "status": "error",
            "data": None,
            "details": exc
        }


@router.put('/operation_id')
async def update_specific_operation(operation_id: int, update_operations:OperationUpdate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = update(operation).where(operation.c.id==operation_id).values(**update_operations.__dict__)
        await session.execute(stmt)
        await session.commit()
        return {
            "status": HTTPException(status_code=200, detail="Successful update"),
        }
    except Exception as exc:
        return{
            "status": "error",
            "data": None,
            "details": exc
        }