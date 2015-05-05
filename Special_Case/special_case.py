""" Special Case Implementation """

class User(object):
    """ User Class """
    
    name = ""
    email = ""
    username = ""
    funds = 123000

    def __init__(self, name, email, username):
        pass

    def get_funds(self):
        return self.funds

    def add_to_funds(self, funds):
        return self.funds + funds

    def changeName(self, name):
        self.name = name


class AnonUser(User):
    """ Anonymous User in the System """

    name = "Anonymous Squirrel"
    email = "anon@ymous.com"
    username = "anon3691"

    def get_funds(self):
        return None

    def add_to_funds(self):
        return None
