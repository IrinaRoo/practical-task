from pydantic import BaseModel
from typing import List


# Модель для объекта произведения искусства
class Artwork(BaseModel):
    objectID: int
    artistDisplayName: str
    isHighlight: bool
    accessionNumber: str
    accessionYear: int
    primaryImage: str
    primaryImageSmall: str
    department: str
    objectName: str
    title: str
    culture: str
    period: str
    artistRole: str
    artistAlphaSort: str
    artistNationality: str
    artistBeginDate: str
    artistEndDate: str
    objectBeginDate: int
    objectEndDate: int
    dimensions: str
    city: str
    state: str
    county: str


# Модель для списка произведений искусства
class WorksOfArts(BaseModel):
    total: int
    objectIDs: List[int]
