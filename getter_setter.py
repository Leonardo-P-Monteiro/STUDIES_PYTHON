


class Person:
    
    def __init__(self, name=str(), height=float(), weight=float(), age=int()):
        self._name = name
        self._height = height
        self._weight = weight
        self._age = age
    
    # Standard format to create a getter. 👴🏻
    def get_name(self):
        return self._name
    # Standard format to create a setter. 👴🏻
    def set_name(self, new_name):
        self._name = new_name

    # Pythonic mode to creat a getter. 😎
    @property
    def age(self):
        return self._age
    
    # Pythonic mode to creat a stter. 😎
    @age.setter
    def age(self, new_value):
        self._age = new_value


    



p1 = Person('Jhon McAffe', 1.73, 67.5, 28)

print('This is the actually name: ', p1.get_name())

p1.set_name('Camala Harrys')

print( 'This is the new name: ', p1.get_name())

print('This is the actually age: ', p1.age)

p1.age = 29

print('This is the new age: ', p1.age)


