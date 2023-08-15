from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from typing import List, Dict
from pydantic import BaseModel

# FastAPI app instance
app = FastAPI()

# SQLAlchemy database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/sqlitedata.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Define data models using SQLAlchemy
class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    genre = Column(String)

    albums = relationship("Album", back_populates="artist")


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist_id = Column(Integer, ForeignKey("artists.id"))

    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    album_id = Column(Integer, ForeignKey("albums.id"))

    album = relationship("Album", back_populates="songs")


# ... Your GET, POST, PUT, DELETE endpoints ...

# Close the database connection when the application shuts down
@app.on_event("shutdown")
def close_db_connection():
    engine.dispose()


# Run migrations to create database tables
Base.metadata.create_all(bind=engine)
