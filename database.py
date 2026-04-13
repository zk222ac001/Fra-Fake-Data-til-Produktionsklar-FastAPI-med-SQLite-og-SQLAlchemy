# Step no : 1 (Import af nødvendige moduler) .......................

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# create_engine: Bruges til at oprette forbindelsen til databasen.
# sessionmaker: Bruges til at oprette database-sessioner (kommunikation med databasen).
# declarative_base: Bruges til at definere dine database-tabeller som Python-klasser (ORM).

# Step no : 2 ( Database URL) ............................... ...............
DATABASE_URL= "sqlite:///./books.db"
# Her definerer du hvilken database du vil bruge.
# "sqlite:///./books.db" betyder:
# sqlite → du bruger SQLite database
# /// → relativ path
# ./books.db → databasefilen ligger i samme mappe som dit projekt

# Step no 3 : ( Oprettelse af database engine) ...............................
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}) 
# engine er selve forbindelsen til databasen.
# connect_args={"check_same_thread": False} --> Bruges kun til SQLite --> Tillader flere threads (fx i webapps som FastAPI) 

# Step no : 4 (Oprettelse af session factory)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# sessionLocal er en factory, der laver nye database-sessioner.
# autocommit=False --> Du skal selv kalde commit() for at gemme ændringer
# autoflush=False --> Data sendes ikke automatisk til databasen før commit
# bind=engine --> Binder sessionen til din database-forbindelse

# Step no 5: Base klasse til modeller
Base = declarative_base()
# Base er en superklasse for alle dine database-tabeller.
# Når du laver en model, inherit du fra Base.
