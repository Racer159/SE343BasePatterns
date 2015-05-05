""" Special Case Implementation """
import random


class User(object):
    """ User Class """
    
    name = ""
    email = ""
    username = ""

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username

    def change_name(self, name):
        self.name = name


class AnonUser(User):
    """ Anonymous User in the System """

    name = "Anonymous Squirrel"
    email = "anon@ymous.com"
    username = "anon3691"

    def __init__(self):
        pass


def main():
    """Randomly select a user type and perform some tasks.
    Demonstrates that an anonymous user can perform similar actions
    without None checks
    """
    num = random.randint(0, 100)

    if num % 2 == 0:
        user = User("Betty White", "bwhite@rit.edu", "wbetty123")
    else:
        user = AnonUser()

    print("Look! The user is not None! " + str(user))

    # Do some stuff with the user
    print("Users Name: " + user.name)
    user.change_name("Major Payne")
    print("Users New Name: " + user.name)

    print("Users Email: " + user.email)

if __name__ == "__main__":
    main()