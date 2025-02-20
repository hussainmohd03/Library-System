# Library System

This is a simple library management system built using Flask. The application allows users to borrow and return books, as well as manage user accounts and book records through an admin interface.

## Project Structure

```
library_system
├── library_system
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── templates
│   ├──admid
│      └── index.html
│   ├── index.html
│   ├── all_books.html
│   ├── book.html
│   ├── register.html
│   ├── login.html
│   ├── return.html

├── static
│   ├──images
├── run.py
└── README.md
```

## Features

- User registration and login
- Browse and search for books
- Borrow and return books
- Admin panel for managing users and books

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd library_system
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Running the Application

To run the application, execute the following command:
```
python run.py
```

The application will be available at `http://127.0.0.1:5000`.

## Usage

- Visit the home page to see recommended books.
- Use the navigation to register, log in, and manage your borrowed books.
- Admin users can access the admin panel to manage users and books.

## License

This project is licensed under the MIT License.
