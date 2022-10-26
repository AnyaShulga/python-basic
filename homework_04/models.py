import os

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)

from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

async_engine: AsyncEngine = create_async_engine(PG_CONN_URI, echo=True)

Session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base(bind=async_engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String(20), unique=True)
    email = Column(String, unique=True)

    posts = relationship('Post', back_populates='user')


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    body = Column(String)

    user = relationship('User', back_populates='posts')
