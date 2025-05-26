from pydantic import BaseModel

class Category(BaseModel):
    CAT_CODE        : int
    CAT_M_CODE      : int
    CAT_NAME        : str
    CAT_NAME_EN     : str
    REMARK          : str
    SORT_SEQ        : int
    USE_YN          : str
    BEST_YN         : str
    BEST_SORT_SEQ   : int
    NEW_YN          : str
    NEW_SORT_SEQ    : int
    PC_ICON_FILE_NM1: str
    MB_ICON_FILE_NM2: str

class Category3(Category):
    pass

class Category2(Category):
    category_3: list[Category3]

class Category1(Category):
    category_2: list[Category2]

class CategoryList(BaseModel):
    success: bool
    categories: list[Category1]


