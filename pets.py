class Pets:
    def __init__(self, breed, name, gender, age):
        self.breed = breed
        self.name = name
        self.gender = gender
        self.age = age

class Cat(Pets):
    def __init__(self, name='', gender='', age=''):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getAge(self):
        return self.age

    def setName(self, name):
        if isinstance(name, str):
            self.name = name
    def setGender(self, gender):
        if (gender.lower() == 'male' or gender.lower() == 'female' or gender.lower() == 'мальчик' or gender.lower() == 'девочка') and isinstance(gender, str):
            self.gender = gender
    def setAge(self, age):
        if age > 0 and isinstance(age, int):
            self.age = age