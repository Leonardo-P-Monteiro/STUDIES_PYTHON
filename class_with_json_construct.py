import json

class Person():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


person_1 = Person('Jhon', 1.73, 67)

with open('person_instance.json', 'w', encoding='utf8') as file:
    json.dump(person_1.__dict__, file, indent= 4)
    file.close()

    