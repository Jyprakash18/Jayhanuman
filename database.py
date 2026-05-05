from sqlalchemy import create_all, create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import config

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    status = Column(String, default="inactive") # active/inactive
    plan_type = Column(String)
    expiry_date = Column(DateTime)
    subscription_id = Column(String)

engine = create_engine(config.DB_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def get_user(user_id):
    return session.query(User).filter_by(user_id=user_id).first()

def add_user(user_id, plan, expiry, sub_id):
    user = get_user(user_id)
    if not user:
        user = User(user_id=user_id)
        session.add(user)
    user.status = "active"
    user.plan_type = plan
    user.expiry_date = expiry
    user.subscription_id = sub_id
    session.commit()
