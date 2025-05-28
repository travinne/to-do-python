from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tasks = relationship('Task', back_populates= 'user')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tasks = relationship('Task', back_populates= 'category')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    complited = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    


