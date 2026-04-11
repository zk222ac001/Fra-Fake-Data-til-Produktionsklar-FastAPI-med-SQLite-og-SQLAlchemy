from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    pages: int

class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True