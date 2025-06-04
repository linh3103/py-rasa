# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from requests import Response

class ActionConfirmOrder(Action):

    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        product = tracker.get_slot("product_name")
        count = tracker.get_slot("count")
        size = tracker.get_slot("size")
        color = tracker.get_slot("color")
        user_name = tracker.get_slot("user_name")
        address = tracker.get_slot("address")
        phone_number = tracker.get_slot("phone_number")

        order_info = f"Vui lòng xác nhận đơn hàng:\n"
        order_info += f"Tên khách hàng: {user_name}\n"
        order_info += f"Sản phẩm: {product}, size: {size}, màu: {color}\n"
        order_info += f"Số lượng: {count}\n"
        order_info += f"Địa chỉ giao hàng: {address}\n"
        order_info += f"Số điện thoại: {phone_number}"

        dispatcher.utter_message(text=order_info)
        
        return []
