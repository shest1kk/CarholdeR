from datetime import datetime

from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

from config import Base


class Roles(Base):
    __tablename__ = 'Roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(String)


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(Integer, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    trip_count = Column(Integer, default=0)
    role = Column(String)


class Cars(Base):
    __tablename__ = 'Cars'

    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    plate = Column(String, primary_key=True, nullable=False)
    color = Column(String, nullable=False)
    available = Column(Boolean, default=True)
    price = Column(Integer, nullable=False)
