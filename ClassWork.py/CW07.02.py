from sqlalchemy import Column, Date, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Session, relationship
 
engine = create_engine('sqlite:///human.db', echo=True)
 
 
class Base(DeclarativeBase):
    pass
 
class Person(Base):
    __tablename__ = "people"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company = relationship('Company', back_populates="users")
    company_id = Column(Integer, ForeignKey("companies.id"))
 
 
class Company(Base):
    __tablename__ = "companies"
 
    id = Column(Integer, primary_key=True, index=True)
    users = relationship('Person', back_populates="company")
    name = Column(String)
 
 
Base.metadata.create_all(bind=engine)
 
 
 
with Session(autoflush=False, bind=engine) as db:
    twitter = Company(name="Twitter")
    google = Company(name="Google")
 
    tim = Person(name="Tim")
    mick = Person(name="Mick")
    alison = Person(name="Alison")
 
    # у компании есть person
    twitter.users = [tim]
    twitter.users = [alison]
    google.users = [mick]
 
    db.add_all([twitter, google])
    db.commit()
 
 
    alice = Person(name="Alice")
    # у person есть компания
    alice.company = google
    db.add(alice)
    db.commit()
 
    # достать всех юзеров
    users = db.query(Person).all()
    for u in users:
        print(f"{u.name} ({u.company.name})")
 
    # получение записей
    tim1 = db.query(Person).filter(Person.name == "Tim").first()
    google1 = db.query(Company).filter(Company.name == "Google").first()
 
    if tim1 != None and google1 != None:
        google1.users.remove(tim1)
        db.commit()
 
    users = db.query(Person).all()
    for u in users:
        print(f"{u.name} ({u.company.name if u.company is not None else None})")
