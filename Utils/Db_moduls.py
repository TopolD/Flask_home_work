from sqlalchemy import Column, Integer, String, ForeignKey
from Utils.Db import Base


class Addresses(Base):
    __tablename__ = 'addresses'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_USER = Column(Integer, ForeignKey('users.ID'))
    Street = Column(String(120), nullable=False)
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
    ID = Column(Integer, primary_key=True, autoincrement=True)
    User_name = Column(String(50), unique=True, nullable=False)
    Password = Column(String(120), unique=True, nullable=False)
    Telephone = Column(Integer)
    Type = Column(Integer, nullable=False)

    def __init__(self, User_name=None, Password=None, Type=None):
        self.User_name = User_name
        self.Password = Password
        self.Type = Type


class Dish(Base):
    __tablename__ = 'dishes'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Dish_name = Column(String(50), unique=True, nullable=False)
    Dish_price = Column(Integer, nullable=False)
    Photo = Column(String(120), nullable=False)
    Category = Column(String(50), ForeignKey('category.Category_name'))

    def __init__(self, Dish_name=None, Dish_price=None, Photo=None, Category=None):
        self.Dish_name = Dish_name
        self.Dish_price = Dish_price
        self.Photo = Photo
        self.Category = Category


class Status(Base):
    __tablename__ = 'status'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Status_name = Column(String(50), unique=True, nullable=False)


class Category(Base):
    __tablename__ = 'category'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Category_name = Column(String(50), unique=True, nullable=False)

    def __init__(self, Category_name=None):
        self.Category_name = Category_name


# cart
class Orders(Base):
    __tablename__ = 'Orders'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_USER = Column(Integer, ForeignKey('users.ID'))
    ID_ADDRESS = Column(Integer, ForeignKey('addresses.ID'))
    Dish_name = Column(String(50))
    Status = Column(String(50), ForeignKey('status.Status_name'))
    Price = Column(Integer, )

    def __init__(self, Dish_name=None):
        self.Dish_name = Dish_name
