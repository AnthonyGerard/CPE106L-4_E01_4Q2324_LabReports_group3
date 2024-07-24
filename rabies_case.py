class RabiesCase:
    def __init__(self, db_manager):
        self.rabies_cases_collection = db_manager.get_rabies_cases_collection()

    def add_rabies_case(self, reporter_id, case_details, reported_date):
        case = {
            "reporter_id": reporter_id,
            "case_details": case_details,
            "reported_date": reported_date
        }
        self.rabies_cases_collection.insert_one(case)

    def get_all_rabies_cases(self):
        return self.rabies_cases_collection.find()
