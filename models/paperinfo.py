from sqlalchemy import Column, Integer, String, Date, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    authors = Column(JSON, nullable=True)  # 리스트 형태로 저장 (예: ["A", "B", "C"])
    journal = Column(String)
    pub_date = Column(Date)
    link_url = Column(String, unique=True)
