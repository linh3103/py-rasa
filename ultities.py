from typing import List, Dict, Any

class Dictable:
    @classmethod
    def list_to_dict_list(cls, items: List[Any]) -> List[Dict]:
        return [item.dict() for item in items]