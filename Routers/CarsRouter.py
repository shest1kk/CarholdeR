from fastapi import APIRouter, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import CarResponse, RequestCars
import crud

CarsRouter = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Вывод всех машин
@CarsRouter.get('/')
async def get_all_cars(db: Session = Depends(get_db)):
    _cars = crud.get_cars(db, 0, 100)
    return CarResponse(cars=_cars).dict(exclude_none=True)


# Вывод машины по ID
@CarsRouter.get('/{id}')
async def get_cars_by_id(id: int, db: Session = Depends(get_db)):
    _cars = crud.get_cars_by_id(db, id)
    return CarResponse(cars=_cars).dict(exclude_none=True)


# Создание машины
@CarsRouter.post('/create')
async def create_cars(request: RequestCars, db: Session = Depends(get_db)):
    crud.create_cars(db, cars=request.parameter)
    return request.dict(exclude_none=True)


# Обновление машины
@CarsRouter.post('/update')
async def update_cars(request: RequestCars, db: Session = Depends(get_db)):
    _cars = crud.update_cars(db, cars_id=request.parameter.id, brand=request.parameter.brand,
                             model=request.parameter.model, plate=request.parameter.plate,
                             color=request.parameter.color, available=request.parameter.available,
                             price=request.parameter.price,
                             image=request.parameter.image)
    return CarResponse(cars=_cars)


# Удаление машины
@CarsRouter.delete('/{id}')
async def delete_cars(id: int, db: Session = Depends(get_db)):
    crud.remove_cars(db, cars_id=id)
    return CarResponse().dict(exclude_none=True)
