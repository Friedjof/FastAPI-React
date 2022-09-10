from sqlalchemy import Column, Integer, String
from database import Base


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String)
    password = Column(String)
