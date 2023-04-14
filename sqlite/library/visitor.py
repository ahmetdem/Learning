
class Visitor:

    def __init__(self, id, name, surname, age, email):
        self.id = int(id)
        self.name = name
        self.surname = surname
        self.age = int(age)
        self.email = email

    def __repr__(self):
        return "Employee({}, {}, {}, {})".format(self.id, self.name, self.surname, self.age)