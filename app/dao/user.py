from app.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, data):
        name = data['username']
        pwd = data['password']
        return self.session.query(User).filter(User.username == name, User.password == pwd).all()

    def create(self, user):
        new_user = User(**user)
        self.session.add(new_user)
        self.session.commit()

    def save_data(self, user):
        self.session.add(user)
        self.session.commit()

