from sqlalchemy import Column,Integer,String
from database import Base


class Blog(Base):
     __tablename__ = 'blogs'

     
     name = Column(String)
     id = Column(Integer,primary_key=True,index=True)
     title = Column(String)
     boby = Column(String)
     name = Column(String)
