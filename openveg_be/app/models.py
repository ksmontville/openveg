from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Restaurant(Base):
    """A class to model restaurants in the database."""
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    vegan = Column(Boolean, default=True)
    web = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    state = Column(String)
    city = Column(String)
    zip = Column(String)
