class User:
    name = None
    email = None
    age = 0
    adress = None

    def __init__(self, namev, emailv, agev, adressv):
        self.name = namev
        self.email = emailv
        self.age = agev
        self.adress = adressv

    def talk(self):
        return f'Hello, I am user and my name is {self.name}'

    def saysAddress(self):
        return f"Good morning, my address is {self.adress}"