class UserService:
    def __init__(self):
        self.users = [
            {"id": 1, "name": "Ahmed Eraqy"},
            {"id": 2, "name": "Omar Nasharty"}
        ]

    def get_users(self):
        return self.users

    def get_user_by_id(self, user_id):
        return next((user for user in self.users if user["id"] == user_id), None)
