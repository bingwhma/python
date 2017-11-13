from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#基类
Base = declarative_base()

class User(Base):
	__tablename__ = 'tbm_users'
	id = Column(Integer, primary_key=True)
	name = Column(String(255))
	password = Column(String(255))


engine = create_engine('mysql://root:root@localhost:3306/test', echo=True)

Base.metadata.create_all(engine)

print(engine.table_names())

#初始化一个Session对象
Session = sessionmaker(bind=engine)
session = Session()

try:
	session.new
	user_1 = User(id=2, name='wang2', password='123') 
	session.add(user_1)
	session.commit()
except:
	session.rollback()

session.query(User).filter_by(name='wang').first()

for name in session.query(User.name).filter_by(password='123'):
	print(name)

session.close()
