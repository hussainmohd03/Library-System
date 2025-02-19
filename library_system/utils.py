import random
from .models import Book

def get_random_elements(db):
    row_count = db.session.query(Book).count()
    random_books = []
    if row_count < 4 and row_count > 0:
        return db.session.query(Book).all()
    
    elif row_count == 0:
        return False
    
    else:
        for _ in range(4):
            result = db.session.query(Book).where(Book.id == random.randint(1, row_count)).scalar()
            random_books.append(result)
        return random_books