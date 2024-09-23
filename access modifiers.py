


class Person:
    
    def __init__(self, name=str(), height=float(), weight=float(), age=int()):
        self.name = name # public access
        self._height = height # protected access
        self.__weight = weight # private access
        self._age = age # protected access
    
    # Standard format to create a getter. 👴🏻
    def get_name(self):
        return self.name
    # Standard format to create a setter. 👴🏻
    def set_name(self, new_name):
        self.name = new_name

    # Pythonic mode to create a getter. 😎
    @property
    def age(self):
        return self._age
    
    # Pythonic mode to create a setter. 😎
    @age.setter
    def age(self, new_value):
        self._age = new_value


################################################################################
################################## OPERATIONS ##################################
################################################################################

p1 = Person('Salor Moon', 1.75, 62.7, 24)

print(p1._Person__weight) # type: ignore # How to access the private attribute.
#Note: This is highly discouraged. If you try access without this standard 
# (_Person__attributename) the interpreter will show a erro.

print(p1._age) # How to access the protected attribute. 

