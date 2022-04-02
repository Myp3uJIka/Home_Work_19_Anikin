from app.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, name):
        return self.session.query(User).filter_by(User.username == name)

    def save_data(self, user):
        self.session.add(user)
        self.session.commit()
