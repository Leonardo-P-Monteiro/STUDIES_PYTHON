class Person():
    var1 = 'Hello, guys!'

    def __init__(self, name=None, age=None, height=None, weight=None):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    @classmethod
    def anonymous_person(cls, age):
        name = 'Anonymous'
        age = age
        return cls(name, age)
    
    @classmethod
    def change_var1(cls, insert):
        cls.var1 = insert
        
    

p1 = Person.anonymous_person(15)

print( p1.name, p1.age)

print(Person.var1)

Person.change_var1('Hi, Daniele!')

print(Person.var1)
