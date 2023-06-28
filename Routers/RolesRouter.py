from fastapi import APIRouter, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestRoles, RoleResponse
import crud

RolesRouter = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Создание роли
@RolesRouter.post('/create')
async def create_roles(request: RequestRoles, db: Session = Depends(get_db)):
    crud.create_roles(db, roles=request.parameter)
    return request.dict(exclude_none=True)


# Вывод всех ролей
@RolesRouter.get('/')
async def get_all_roles(db: Session = Depends(get_db)):
    _roles = crud.get_roles(db, 0, 100)
    return RoleResponse(roles=_roles).dict(exclude_none=True)


# Вывод роли по ID
@RolesRouter.get('/{id}')
async def get_roles_by_id(id: int, db: Session = Depends(get_db)):
    _roles = crud.get_roles_by_id(db, id)
    return RoleResponse(roles=_roles).dict(exclude_none=True)


# Обновление роли
@RolesRouter.post('/update')
async def update_roles(request: RequestRoles, db: Session = Depends(get_db)):
    _roles = crud.update_roles(db, roles_id=request.parameter.id, name=request.parameter.name,
                               permissions=request.parameter.permissions)
    return RoleResponse(roles=_roles)


# Удаление роли
@RolesRouter.delete('/{id}')
async def delete_roles(id: int, db: Session = Depends(get_db)):
    crud.remove_roles(db, roles_id=id)
    return RoleResponse().dict(exclude_none=True)
