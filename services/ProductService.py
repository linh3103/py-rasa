import httpx
from schemas.Product import ProductList
from constants import BASE_URL

async def fetchProductsByCatCode(cat_code: int):
    async with httpx.AsyncClient() as client:
        END_POINT = "filter/product/list"
        url = f"{BASE_URL}/{END_POINT}"
        body = {"cat_code": cat_code}

        response = await client.post(url, json=body)

        if response.status_code == 200:
            data = response.json()
            return ProductList(**data)
        else: 
            raise Exception(f"Error fetching products: {response.status_code}")