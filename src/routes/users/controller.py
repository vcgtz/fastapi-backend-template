class UserController:
    @staticmethod
    def get_all_users():
        return {
            "method": "GET",
            "url": "/users",
            "content": "Get all users",
        }

    @staticmethod
    def get_user(user_id: int):
        return {
            "method": "GET",
            "url": "/users/{}".format(user_id),
            "content": "Get one user",
        }

    @staticmethod
    def store_user(user: dict):
        return {
            "method": "POST",
            "url": "/users",
            "content": "Store one user",
        }

    @staticmethod
    def update_user(user_id: int):
        return {
            "method": "PUT",
            "url": "/users/{}".format(user_id),
            "content": "Update one user",
        }

    @staticmethod
    def delete_user(user_id: int):
        return {
            "method": "PUT",
            "url": "/users/{}".format(user_id),
            "content": "Delete one user",
        }
