from sqlalchemy import Integer, String, DateTime, ForeignKey, Column
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime
from library_system import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(250), nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    
    def __repr__(self):
        return f"{self.full_name}"

class Book(db.Model):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    description = Column(String(7000), nullable=False)
    language = Column(String(250), nullable=False)
    genre = Column(String(250), nullable=False)
    total_copies = Column(Integer, nullable=False)
    location = Column(String(250), nullable=False)
    img_url = Column(String(250), nullable=False)
    borrowed_copies = Column(Integer, nullable=False, default=0)
    borrowed = relationship("Borrow", back_populates="book")
    ebook_location = Column(String(250), nullable=True)


    def __str__(self):
        return f'{self.title}'

class Borrow(db.Model):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True)
    date_borrowed = Column(DateTime, nullable=False, default=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book", back_populates="borrowed")

    def __repr__(self):
        return f'{self.book}'