from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from database import engine

Base = declarative_base()

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    patient = Column(String)
    doctor = Column(String)
    slot = Column(String)
    status = Column(String)


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    preferred_language = Column(String)
    preferred_doctor = Column(String)


Base.metadata.create_all(bind=engine)