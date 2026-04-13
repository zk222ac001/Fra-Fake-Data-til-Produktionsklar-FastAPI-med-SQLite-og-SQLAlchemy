# skridt no 1 : importere FastAPI klassen fra fastapi biblioteket

# Depends bruges til dependency injection (meget vigtigt i FastAPI)
# Det betyder: Du kan “injecte” funktioner automatisk ,Typisk brugt til: (Database connection ,Authentication ,Shared logic)
from fastapi import FastAPI , Depends

# Session er din forbindelse til databasen i SQLAlchemy
# Den bruges til at: --> Læse data (SELECT) --> Gemme data (INSERT) --> Opdatere data (UPDATE) --> Slette data (DELETE)
from sqlalchemy.orm import Session
from database import sessionLocal, engine
import models , schemas

# Create the database tables
models.Base.metadata.create_all(bind=engine)
# skridt no 2 : oprette en instans af FastAPI klassen
app = FastAPI()

# Dependency (DB session)
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# skridt no 3 : definere en rute ved hjælp af app.get() dekoratoren
# Get all books
@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

# Get specific book by book_ID 
@app.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

# Add New Resource
@app.post("/books")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(title=book.title, author=book.author, pages=book.pages)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# update existing resource
@app.put("/books/{book_id}")
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book: models.Book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        return {"error": "Book not found"}
    db_book.title = book.title
    db_book.author = book.author
    db_book.pages = book.pages
    db.commit()
    db.refresh(db_book)
    return db_book

# Delete book by Id
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):    
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        return {"error": "Book not found"}
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"} 

# Search book by Title
@app.get("/books/search/")
def search_books(title: str, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.title.contains(title)).all()

@app.get("/books/sort/")
def sort_books(sort_by: str, db: Session = Depends(get_db)):
    if sort_by == "title":
        return db.query(models.Book).order_by(models.Book.title).all()
    elif sort_by == "author":
        return db.query(models.Book).order_by(models.Book.author).all()
    elif sort_by == "pages":
        return db.query(models.Book).order_by(models.Book.pages).all()
    else:
        return {"error": "Invalid sort parameter"}
