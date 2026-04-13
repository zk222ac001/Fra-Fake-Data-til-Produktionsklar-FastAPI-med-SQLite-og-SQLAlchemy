from pydantic import BaseModel
# BaseModel → Grundklassen i Pydantic
# Bruges til: --> Data validering --> API request/response modeller (fx i FastAPI)

# BookCreate (input model) ......................................
# Denne klasse bruges når du opretter en bog (POST request)
class BookCreate(BaseModel):
    title: str
    author: str
    pages: int

# BookResponse (output model)..............................................
# Denne bruges når du returnerer data fra API’et
class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True
