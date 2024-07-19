class VaccinationRecord:
    def __init__(self, db_manager):
        self.vaccination_records_collection = db_manager.get_vaccination_records_collection()

    def add_vaccination_record(self, pet_id, vaccine_name, vaccination_date, veterinarian_id):
        record = {
            "pet_id": pet_id,
            "vaccine_name": vaccine_name,
            "vaccination_date": vaccination_date,
            "veterinarian_id": veterinarian_id
        }
        self.vaccination_records_collection.insert_one(record)
