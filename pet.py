class Pet:
    def __init__(self, db_manager):
        self.pets_collection = db_manager.get_pets_collection()

    def add_pet(self, owner_id, pet_name, species, age, vaccination_status):
        pet = {
            "owner_id": owner_id,
            "pet_name": pet_name,
            "species": species,
            "age": age,
            "vaccination_status": vaccination_status
        }
        self.pets_collection.insert_one(pet)
