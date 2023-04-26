import pymongo


class Config:
    def __init__(self) -> None:
        self.uri = 'mongodb://root:UtyCantik12@203.194.113.203:27017'
        self.client = pymongo.MongoClient()
        self.dblist = self.client.list_database_names()
        self.database = None
        self.collection_list = None
        self.collection = None

    def select_database(self, database_name):
        if "mongo" not in self.dblist:
            self.database = self.client[database_name]
            print("Database created! 🤩")
        else:
            self.database = self.client[database_name]

        self.collection_list = self.database.list_collection_names()

    def select_collection(self, collection_name):
        if collection_name not in self.collection_list:
            self.collection = self.database[collection_name]
            print("Collection created! 🤩")
        else:
            self.collection = self.database[collection_name]
            