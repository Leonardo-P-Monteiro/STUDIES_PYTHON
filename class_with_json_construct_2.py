import json

class Person():
    
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

with open('person_instance.json', 'r', encoding='utf8') as file:
    file_jason = json.load(file)

person_1 = Person(**file_jason)
person_2 = Person('Marie', 1.5, 90)
print(person_2.cabelo) # type: ignore


