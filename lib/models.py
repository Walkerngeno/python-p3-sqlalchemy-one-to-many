# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    reviews = relationship("Review", back_populates="game")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    game_id = Column(Integer, ForeignKey("games.id"))
    
    game = relationship("Game", back_populates="reviews")
