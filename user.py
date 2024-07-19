import bcrypt

class User:
    def __init__(self, db_manager):
        self.users_collection = db_manager.get_users_collection()

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

    def register_user(self, name, email, password, role):
        hashed_password = self.hash_password(password)
        user = {
            "name": name,
            "email": email,
            "password": hashed_password,
            "role": role
        }
        self.users_collection.insert_one(user)

    def authenticate_user(self, email, password):
        user = self.users_collection.find_one({"email": email})
        if user and self.check_password(password, user["password"]):
            return user
        return None
