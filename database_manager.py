from pymongo import MongoClient

class DatabaseManager:
    def __init__(self, db_name="anti_rabies_db"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.users_collection = self.db["users"]
        self.pets_collection = self.db["pets"]
        self.vaccination_records_collection = self.db["vaccination_records"]
        self.rabies_cases_collection = self.db["rabies_cases"]

    def get_users_collection(self):
        return self.users_collection

    def get_pets_collection(self):
        return self.pets_collection

    def get_vaccination_records_collection(self):
        return self.vaccination_records_collection

    def get_rabies_cases_collection(self):
        return self.rabies_cases_collection
