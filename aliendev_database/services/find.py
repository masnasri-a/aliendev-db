class Find:
    def __init__(self, collection) -> None:
        self.collection = collection    
    
    def find_one(self, key, value):
        return self.collection.find_one({key: value})

    def find_many(self, key=None, value=None):
        if not key or not value:
            return self.collection.find({})
        else:
            return self.collection.find({key: value})

    def pagination(self, page=1, limit=5, key=None, value=None):
        if not key or not value:
            offset = (page - 1) * limit
            return self.collection.find({}).skip(offset).limit(limit)
        else:
            offset = (page - 1) * limit
            return self.collection.find({key: value}).skip(offset).limit(limit)
