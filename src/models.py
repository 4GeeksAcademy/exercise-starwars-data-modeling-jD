import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Date, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True , autoincrement=True)
    population = Column(Integer, nullable=False)
    climate= Column(Enum(),nullable=False)
    name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    date = Column(Date, default=func.current_date(), nullable=False)
    
    favorites = relationship("Favorite", back_populates="user")


class Favorite(Base):
    __tablename__ = "favorite"

    id= Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    character_id= Column(Integer, ForeignKey("character.id"), nullable=True)
    planet_id = Column(Integer,ForeignKey("planet.id"), nullable=True)

    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")

    
class Characters(Base):
    __tablename__= "character"
    id= Column(Integer, primary_key=True)
    name=Column(String(250), nullable=False)
    birthday_year= Column(String(250), nullable=False)
    gender = Column(String(50))
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
