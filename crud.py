from sqlalchemy.orm import Session
from models.models import Roles, Users, Cars
from schemas import RolesSchema, UsersSchema, CarsSchema


# Получение списка всех автомобилей
def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cars).offset(skip).limit(limit).all()


# Получение автомобиля по ID
def get_cars_by_id(db: Session, cars_id: int):
    return db.query(Cars).filter(cars_id == Cars.id).first()


# Создание автомобиля
def create_cars(db: Session, cars: CarsSchema):
    _cars = Cars(id=cars.id, brand=cars.brand, model=cars.model, plate=cars.plate, color=cars.color,
                 available=cars.available, price=cars.price, image=cars.image)
    db.add(_cars)
    db.commit()
    db.refresh(_cars)
    return _cars


# Удаление машины
def remove_cars(db: Session, cars_id: int):
    _cars = get_cars_by_id(db=db, cars_id=cars_id)
    db.delete(_cars)
    db.commit()


# Обновление данных автомобиля
def update_cars(db: Session, cars_id: int, brand: str, model: str, plate: str, color: str, available: bool, price: int,
                image: str):
    _cars = get_cars_by_id(db=db, cars_id=cars_id)

    _cars.brand = brand
    _cars.model = model
    _cars.plate = plate
    _cars.color = color
    _cars.available = available
    _cars.price = price
    _cars.image = image
    db.commit()
    db.refresh(_cars)
    return _cars


# Получение списка всех юзеров
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()


# Получение юзера по ID
def get_users_by_id(db: Session, users_id: int):
    return db.query(Users).filter(users_id == Users.id).first()


# Создание пользователя
def create_user(db: Session, users: UsersSchema):
    _user = Users(id=users.id, username=users.username, email=users.email, phone=users.phone, password=users.password,
                  registered_at=users.registered_at, trip_count=users.trip_count, role=users.role)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


# Удаление юзера
def remove_users(db: Session, users_id: int):
    _users = get_users_by_id(db=db, users_id=users_id)
    db.delete(_users)
    db.commit()


# Обновление юзера
def update_users(db: Session, users_id: int, username: str, email: str, phone: str, password: str, registered_at: str,
                 trip_count: int, role: str):
    _users = get_users_by_id(db=db, users_id=users_id)
    _users.username = username
    _users.email = email
    _users.phone = phone
    _users.password = password
    _users.registered_at = registered_at
    _users.trip_count = trip_count
    _users.role = role
    db.commit()
    db.refresh(_users)
    return _users


# Получение списка всех ролей
def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Roles).offset(skip).limit(limit).all()


# Получение роли по ID
def get_roles_by_id(db: Session, roles_id: int):
    return db.query(Roles).filter(roles_id == Roles.id).first()


# Создание роли
def create_roles(db: Session, roles: RolesSchema):
    _roles = Roles(name=roles.name, permissions=roles.permissions)
    db.add(_roles)
    db.commit()
    db.refresh(_roles)
    return _roles


# Удаление роли
def remove_roles(db: Session, roles_id: int):
    _roles = get_roles_by_id(db=db, roles_id=roles_id)
    db.delete(_roles)
    db.commit()


# Обновление роли
def update_roles(db: Session, roles_id: int, name: str, permissions: str):
    _roles = get_roles_by_id(db=db, roles_id=roles_id)
    _roles.name = name
    _roles.permissions = permissions
    db.commit()
    db.refresh(_roles)
    return _roles
