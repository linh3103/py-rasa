from pydantic import BaseModel
from ultities import Dictable

class Product(BaseModel):
    product_cd: str
    product_nm: str
    option_nm: str
    supply_price: int
    sale_price: int
    point: float
    review_cnt: int
    file_nm: str

class ProductList(BaseModel, Dictable):
    success: bool
    list: list[Product]

    