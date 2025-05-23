from schemas.Category import CategoryList
from constants import BASE_URL
import httpx

async def getProductCategories():
    url = f"{BASE_URL}/filter/category/list"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return CategoryList(**data)
        else:
            raise Exception(f"Error fetching categories: {response.status_code}")
    