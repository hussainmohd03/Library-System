# Personal Library Management System

This project is a web-based application built with Flask to help you **manage and track your personal book collection**. You can add books, search and browse your library, record borrowing activity, and even manage e-books. An admin interface is included for easy management.

---

## Features

- **Personal Book Tracking:** Add, edit, and view your books.
- **Borrow & Return:** Track which books are borrowed and returned.
- **E-Book Support:** Download e-books stored in your collection.
- **Search & Browse:** Quickly find books by title or author.
- **User Authentication:** Register and log in to keep your data secure.
- **Admin Panel:** Manage your collection and borrowing records with a user-friendly interface.

---

## Folder Structure

```
Library-System-main/
│
├── run.py
├── requirements.txt
├── README.md
└── library_system/
    ├── __init__.py
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── routes.py
    ├── utils.py
    ├── static/
    │   ├── files/      # E-book PDF files
    │   └── images/     # Book cover images and other images
    └── templates/
        ├── base.html
        ├── index.html
        ├── all_books.html
        ├── book.html
        ├── login.html
        ├── register.html
        ├── return.html
        └── admin/
            └── index.html
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd Library-System-main
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

---

## Running the Application

Just run:

```sh
python run.py
```

- The application will **automatically create the database** (`library_system.db`) if it does not already exist.
- Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Usage

- **Home:** See recommended books from your collection.
- **Books:** Browse or search your entire library by author or by book name .
- **Book Details:** View details, mark as borrowed/returned, or download e-books.
- **Register/Login:** Secure your library with user authentication.
- **Return:** Mark books as returned.
- **Admin Panel:** Manage your collection and borrowing records (admin only).

---

## Admin Panel

- Accessible at `/admin` after logging in as the admin user (user with ID 1).
- Add, edit, or remove books and manage borrowing records.
- To add an e-book, set the book's location to `E-Book` and provide the PDF filename in the "E-Book location" field. Place the PDF in `library_system/static/files/`.

---

## Customization

- **Book Images:** Place cover images in `library_system/static/images/books/` and set the `img_url` field accordingly.
- **E-Books:** Place PDF files in `library_system/static/files/`.


