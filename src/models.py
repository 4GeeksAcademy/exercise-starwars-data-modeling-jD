import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Date
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
    climate= Column(Enum("arid", "temperate", "tropical","frozen","murky"),nullable=False)
    name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), unique=True,nullable=False)
    email = Column(String(250), unique=True,nullable=False)
    password = Column(String(250), unique=True,nullable=False)
    
class Characters(Base):
    __tablename__= "character"
    id= Column(Integer, primary_key=True)
    name=Column(String(250), nullable=False)
    birth_year= Column(String(250), nullable=False)
    gender = Column(String(50))
    species= Column(String(20))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
