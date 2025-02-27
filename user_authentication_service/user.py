#!/usr/bin/env python3
"""user model file"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# create a declaration base
Base = declarative_base()


class User(Base):
    """
    create a SQLAlchemy model for a database
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
