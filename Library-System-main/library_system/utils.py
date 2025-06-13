import random
from .models import Book

def get_random_elements(db):
    db_content = db.session.query(Book).all()
    row_count = len(db_content)
    
    if row_count < 4 and row_count > 0:
        return db_content
    
    elif row_count == 0:
        return False
    
    else:
        random_books = random.sample(db_content, 4)

        return random_books
