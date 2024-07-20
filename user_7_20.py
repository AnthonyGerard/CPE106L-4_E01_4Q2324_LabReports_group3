
class User:
    def __init__(self, db_manager):
        self.users_collection = db_manager.get_users_collection()

    def register_user(self, name, email, password, role):
        user = {
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }
        self.users_collection.insert_one(user)

    def authenticate_user(self, email, password):
        user = self.users_collection.find_one({"email": email})
        if user:
            return user
        return None
