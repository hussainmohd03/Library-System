from flask import render_template, request, redirect, flash, url_for, send_from_directory
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Book, Borrow
from .forms import LoginForm, RegisterForm, ReturnForm
from . import db
from .utils import get_random_elements
from . import app
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def home():
    books_to_recommend = get_random_elements(db)
    return render_template('index.html', recommended_books = books_to_recommend)


@app.route('/books', methods=["GET", "POST"])
def all_books():
    
    if request.method == "POST":
        search_query = request.form.get('search').lower().strip()
        books = db.session.query(Book).filter(
            Book.title.ilike(f'%{search_query}%') | 
            Book.author.ilike(f'%{search_query}%')
        ).all()
        return render_template('all_books.html', books=books)

    result = db.session.query(Book).all()
    return render_template('all_books.html', books=result)

@app.route('/book/<int:bookID>')
def display_book(bookID):
    result = db.session.query(Book).where(Book.id == bookID).scalar()
    return render_template('book.html', book=result)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username_exist = db.session.query(User).where(User.username == form.username.data).scalar()

        if username_exist:
            flash("Username already used, try another one")
            return redirect(url_for('register'))

        else:
            new_user = User(full_name=form.fullname.data,
                            username=form.username.data,
                            password=generate_password_hash(password=form.password.data, method='pbkdf2:sha256', salt_length=8))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        return redirect(url_for('home'))

    return render_template("register.html", form=form)



@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.query(User).filter_by(username=form.username.data).first() 
        if not user:
            flash('Username does not exist, please try again.')
            return redirect(url_for('login'))
                
        elif not check_password_hash(user.password, form.password.data):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
            
        else:
            login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route('/return', methods=['GET','POST'])
@login_required
def return_book():
    form = ReturnForm()
    form.book_name.choices = [book for book in db.session.query(Borrow).where(Borrow.user_id == current_user.username).all()]
    if form.validate_on_submit():
        book = db.session.query(Book).where(Book.title == form.book_name.data).scalar()
        borrow = db.session.query(Borrow).where(Borrow.book_id == book.id).first()
        book.borrowed_copies -= 1
        db.session.delete(borrow)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('return.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/borrow/<int:bookID>')
@login_required
def borrow(bookID):
    book_to_borrow = db.session.query(Book).where(Book.id == bookID).scalar()
    if book_to_borrow.borrowed_copies == book_to_borrow.total_copies:
        flash('All copies of this book are borrowed, try another book') 
        return redirect(url_for('display_book', bookID=bookID))
    elif book_to_borrow.borrowed_copies < book_to_borrow.total_copies and book_to_borrow.borrowed_copies >= 0:
        book_to_borrow.borrowed_copies += 1
        new_borrow = Borrow(user_id=current_user.username,book_id=bookID)
        db.session.add(new_borrow)
        db.session.commit()
        return redirect(url_for('home'))

#@app.route('/admin')
#@login_required
#def admin_page():
#    pass     

@app.route('/download/<path:filename>')
@login_required
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],path=filename)
