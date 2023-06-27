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
    id: Optional[int] = SERIAL
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


class RequestRoles(BaseModel):
    parameter: RolesSchema = Field(...)


class RequestUsers(BaseModel):
    parameter: UsersSchema = Field(...)


class Response(GenericModel, Generic[T]):
    result: Optional[T]
