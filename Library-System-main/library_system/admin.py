from flask import redirect, url_for
from flask_login import current_user
from flask_admin import AdminIndexView, expose, Admin
from flask_admin.contrib.sqla import ModelView
from . import app, db, models


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1  # Only admins can access
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('home'))  # Redirect to home if unauthorized

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated or not current_user.id == 1:
            return redirect(url_for('home'))
        return super().index()
    
class UserView(AdminModelView):
    column_exclude_list = ['password']
    can_edit = False
    can_create = False

class BorrowView(AdminModelView):
    can_delete = False
    can_create = False
    can_edit = False 
    column_list = ['user_id', 'book', 'date_borrowed']

class BookView(AdminModelView):
    column_exclude_list = ['description']

    


admin = Admin(app, index_view=MyAdminIndexView())

admin.add_view(UserView(models.User, db.session))
admin.add_view(BookView(models.Book, db.session))
admin.add_view(BorrowView(models.Borrow, db.session))
