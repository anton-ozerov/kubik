from pydantic import BaseModel


class ObjectModel(BaseModel):
    id: int
    title: str
    current_price: int
    old_price: int | None = None
    sale_percent: int | None = None


class ResultModel(BaseModel):
    current_page: int
    max_page: int
    objects: list[ObjectModel]
