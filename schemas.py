from datetime import datetime
from typing import Optional, Generic, TypeVar

from dns.version import SERIAL
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class RolesSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    permissions: Optional[str] = None

    class Config:
        orm_mode = True


class UsersSchema(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None
    password: Optional[str] = None
    registered_at: Optional[datetime] = None
    trip_count: Optional[int] = None
    role: Optional[str] = None

    class Config:
        orm_mode = True


class CarsSchema(BaseModel):
    id: Optional[int] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    plate: Optional[str] = None
    color: Optional[str] = None
    available: Optional[bool] = None
    price: Optional[int] = None
    image: Optional[str] = None

    class Config:
        orm_mode = True


class RequestRoles(BaseModel):
    parameter: RolesSchema = Field(...)


class RequestUsers(BaseModel):
    parameter: UsersSchema = Field(...)


class RequestCars(BaseModel):
    parameter: CarsSchema = Field(...)


class CarResponse(GenericModel, Generic[T]):
    cars: Optional[T]


class UserResponse(GenericModel, Generic[T]):
    users: Optional[T]


class RoleResponse(GenericModel, Generic[T]):
    roles: Optional[T]
