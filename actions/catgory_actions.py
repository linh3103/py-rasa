import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, List, Dict, Any

from services.CategoryService import getProductCategories

class fetchCategory(Action):
    def name(self) -> Text:
        return "action_fetch_categories"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            # result = await getProductCategories()
            # Giả sử result.categories là list các object Category
            # categories = [cat.dict() for cat in result.categories]
            dispatcher.utter_message(json_message={"message": "100 categories"})
        except Exception as e:
            dispatcher.utter_message(json_message={"message": "Error fetching categories", "error": str(e)})
        return []