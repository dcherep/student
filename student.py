from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, relationship

engine = create_engine("postgresql://admin:12345@217.71.129.139:6075/my_database")
class Base(DeclarativeBase): pass
class Group(Base):
    __tablename__="groups"
    id = Column(Integer, primary_key=True, index=True)
    title= Column(String, nullable=False)
    students = relationship("Student", back_populates="group", lazy="joined")

class Student(Base):
    __tablename__="students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patr = Column(String)
    gender=Column(String)
    logo=Column(String)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    group=relationship("Group", back_populates="students",lazy="joined")

def create():
    Base.metadata.create_all(bind=engine)
    print("База данных и таблица созданы")





