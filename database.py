class Database:
    def save(self, data):
        raise NotImplementedError
    
class UserRepository:
    def __init__(self, db: Database):
        self.db = db

    def create_user(self, user):
        return self.db.save(user)