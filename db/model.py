__all__ = ['User']

import enum
from sqlalchemy import Column, Integer, String, Float, Enum, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# -------------------- ENUM ----------------------------------
class UserStatus(enum.Enum):
    ACTIVES = 'actives'
    BLOCK = 'block'


class UserRole(enum.Enum):
    CLIENT = 'client'
    ADMIN = 'admin'


# ----------------- MODELS -----------------------------------
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Numeric(precision=100))
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    user_name = Column(String(50), unique=True, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.CLIENT)
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVES)
    password = Column(String(50), unique=True)
    balance = Column(Float, unique=True, default=0.0)
