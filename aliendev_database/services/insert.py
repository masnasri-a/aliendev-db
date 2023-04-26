from hashlib import sha256
import json

class Insert:

    def __init__(self, collection) -> None:
        self.collection = collection

    def insert_one(self, data: dict, _id=None):
        if not _id:
            new_data = {}
            json_str = json.dumps(data, sort_keys=True)
            _id = sha256(json_str.encode()).hexdigest()
            new_data['_id'] = _id
            new_data.update(data)
            data = new_data
        self.collection.insert_one(data)
        
    def insert_many(self, data:list):
        for index, detail in enumerate(data):
            if '_id' not in detail:
                json_str = json.dumps(detail, sort_keys=True)
                _id = sha256(json_str.encode()).hexdigest()
                data[index]['_id'] = _id
        self.collection.insert_many(data)