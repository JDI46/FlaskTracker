from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

alchemy = SQLAlchemy()

class Base(DeclarativeBase):
    pass