import httpx
from schemas.Product import ProductList
from constants import BASE_URL
from typing import Dict, Text, Any

async def fetchProductsByCatCode(payload: Dict[Text, Any]):
    async with httpx.AsyncClient() as client:
        END_POINT = "filter/product/list"
        url = f"{BASE_URL}/{END_POINT}"
        response = await client.post(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            # Khởi tạo ProductList, sau đó dùng phương thức list_to_dict_list để trả về list các dict
            product_list = ProductList(**data)
            return ProductList.list_to_dict_list(product_list.list)
        else:
            raise Exception(f"Error fetching products: {response.status_code}")