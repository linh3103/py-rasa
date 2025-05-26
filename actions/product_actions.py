from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, List, Dict, Any
from services.ProductService import fetchProductsByCatCode

class productActions(Action):
    def name(self) -> Text:
        return "action_fetch_products_by_cat_code"
    
    async def run(self,
              dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cat_code = tracker.get_slot("cat_code")
        row_count = tracker.get_slot("row_count")

        if not row_count:
            row_count = 5

        payload = {
            "cat_code": cat_code,
            "row_count": row_count
        }

        print(payload)

        try:
            products = await fetchProductsByCatCode(payload)

            if not products:
                dispatcher.utter_message(json_message={"message": "No data"})
                return []
            dispatcher.utter_message(json_message=products)
        except Exception as e:
            print("Error:", e)
            dispatcher.utter_message(json_message={"message": "Error fetching products", "error": str(e)})
        
        return []

