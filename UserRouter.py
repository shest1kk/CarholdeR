from fastapi import APIRouter, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestUsers, Response
import crud

UsersRouter = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Создание юзера
@UsersRouter.post('/create')
async def create_users(request: RequestUsers, db: Session = Depends(get_db)):
    crud.create_user(db, users=request.parameter)
    return request.dict(exclude_none=True)


# Вывод всех пользователей
@UsersRouter.get('/')
async def get_all_users(db: Session = Depends(get_db)):
    _users = crud.get_users(db, 0, 100)
    return Response(result=_users).dict(exclude_none=True)


# Вывод пользователя по ID
@UsersRouter.get('/{id}')
async def get_users_by_id(id: int, db: Session = Depends(get_db)):
    _users = crud.get_users_by_id(db, id)
    return Response(result=_users).dict(exclude_none=True)


# Обновление юзера
@UsersRouter.post('/update')
async def update_users(request: RequestUsers, db: Session = Depends(get_db)):
    _users = crud.update_users(db, users_id=request.parameter.id, username=request.parameter.username,
                               email=request.parameter.email, phone=request.parameter.phone,
                               password=request.parameter.password, registered_at=request.parameter.registered_at,
                               trip_count=request.parameter.trip_count, role=request.parameter.role)
    return Response(result=_users)


# Удаление пользователя
@UsersRouter.delete('/{id}')
async def delete_users(id: int, db: Session = Depends(get_db)):
    crud.remove_users(db, users_id=id)
    return Response().dict(exclude_none=True)

