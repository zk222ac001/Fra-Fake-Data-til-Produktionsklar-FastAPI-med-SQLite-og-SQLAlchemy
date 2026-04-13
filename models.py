# Step no 1 : impotere bibloteket
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

# Integer, String → Datatyper til databasen (tal og tekst)
# Mapped → Bruges til type-annotation (moderne SQLAlchemy 2.0 stil)
# mapped_column → Definerer en kolonne i databasen
# Base → Din baseklasse (typisk lavet med declarative_base()), som alle modeller arver fra

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    author: Mapped[str] = mapped_column(String, index=True)
    pages: Mapped[int] = mapped_column(Integer)
