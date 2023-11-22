from typing import Annotated

from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from Utils.Db import Base
from sqlalchemy.orm import relationship

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class Addresses(Base):
    __tablename__ = 'addresses'
    ID: Mapped[intpk]
    ID_USER: Mapped[int] = mapped_column(ForeignKey('users.ID'), nullable=True)
    Street: Mapped[str] = mapped_column(nullable=False)
    House = Column(String(50))
    Town = Column(String(50))
    Apt = Column(Integer)

    def __init__(self, Street=None, House=None, Town=None, Apt=None):
        self.Street = Street
        self.House = House
        self.Town = Town
        self.Apt = Apt


class User(Base):
    __tablename__ = 'users'
    ID: Mapped[intpk]
    User_name = Column(String(50), unique=True, nullable=False)
    Password = Column(String(120), unique=True, nullable=False)
    Telephone = Column(Integer)
    Type = Column(Integer, nullable=False)

    def __init__(self, User_name=None, Password=None, Type=None, Telephone=None):
        self.User_name = User_name
        self.Password = Password
        self.Telephone = Telephone
        self.Type = Type


class Dish(Base):
    __tablename__ = 'dishes'
    ID: Mapped[intpk]
    Dish_name = Column(String(50), unique=True, nullable=False)
    Dish_price = Column(String(50), nullable=False)
    Photo = Column(String(120), nullable=False)
    Category = Column(String(50), ForeignKey('category.Category_name'))

    def __init__(self, Dish_name=None, Dish_price=None, Photo=None, Category=None):
        self.Dish_name = Dish_name
        self.Dish_price = Dish_price
        self.Photo = Photo
        self.Category = Category


class Status(Base):
    __tablename__ = 'status'
    ID: Mapped[intpk]
    Status_name = Column(String(50), unique=True, nullable=False)


class Category(Base):
    __tablename__ = 'category'
    ID: Mapped[intpk]
    Category_name = Column(String(50), unique=True, nullable=False)

    def __init__(self, Category_name=None):
        self.Category_name = Category_name


# cart
class Orders(Base):
    __tablename__ = 'orders'
    ID: Mapped[intpk]
    User_id = Column(Integer, ForeignKey('users.ID'))
    Dish_name = Column(String(50))
    Status = Column(String(50))
    Price = Column(String(50))

    def __init__(self, Dish_name=None, User_id=None, Status=None, Price=None):
        self.User_id = User_id
        self.Dish_name = Dish_name
        self.Status = Status
        self.Price = Price
