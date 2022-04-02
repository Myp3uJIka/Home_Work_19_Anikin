from app.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session
