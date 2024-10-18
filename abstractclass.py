from abc import ABC, abstractmethod

class Human(ABC):

    def __init__(self, name, height, weight):
        self._name = name
        self._height = height
        self._weight = weight
        self._walk = False

    @property  # Example of use abstract method with getter/setter with pythonic mode.
    @abstractmethod
    def name(self):
        ...

    @name.setter # Example of use abstract method with getter/setter with pythonic mode.
    @abstractmethod
    def name(self, new_name):
        ...
    @property  # Example of use abstract method with getter/setter with pythonic mode.
    @abstractmethod
    def height(self):
        ...

    @height.setter # Example of use abstract method with getter/setter with pythonic mode.
    @abstractmethod
    def height(self, new_height):
        ...
    @property  # Example of use abstract method with getter/setter with pythonic mode.
    @abstractmethod
    def weight(self):
        ...

    @weight.setter # Example of use abstract method with getter/setter with pythonic mode.
    @abstractmethod
    def weight(self, new_weight):
        ...

    @classmethod # Example of use abstract method with class method.
    @abstractmethod
    def anonymous(cls, heigth, weight):
        ...

    @staticmethod
    @abstractmethod
    def information():
        pass

    @abstractmethod # Example of use abstract method with a normal method.
    def speak(self, msg):
        pass

    def walk(self):  # Example of use concret method into a abstract class. 
        if self._walk:
            print(f'{self.name} stoped to walk.')
            self._walk = False
        else:
            print(f'{self.name} started to walk.')
            self._walk = True
    

class Person(Human):
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    @classmethod
    def anonymous(cls, height, weight):
        anonymous = Person('Anonymous', height, weight)
        return anonymous

    @staticmethod
    def information():
        return dir(Person)

    def speak(self, msg):
        print(f'{self.name} is speaking: {msg}')

if __name__ == "__main__":
    p1 = Person('Oliver', 1.70, 67)
    print('Calling the height: ', p1.height)
    print('Calling the weight: ', p1.weight)
    print('Calling the name: ', p1.name)
    p1.speak('Hi! I live on USA.')
    p1.walk()
    p1.walk()
    

    p2 = Person.anonymous(1.6, 78)
    print(p2.name)

