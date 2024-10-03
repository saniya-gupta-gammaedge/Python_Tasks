from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class User(Base):
    __tablename__="student1"
    sid=Column(Integer,primary_key = True)
    sname=Column(String(50))

engine=create_engine('mysql+pymysql://root:new_password@localhost/userdb')
Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

new_user=User(sname="Saniya")
session.add(new_user)
session.commit()
print("New user added")
