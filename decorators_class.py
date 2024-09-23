################################################################################
########################### DECORATORS WITH CLASSES ############################
################################################################################


def mynewrepr(cls):
    
    def wrapper_mynewrapr(self):
        representation = ', '.join(f'{key}: {value!r}' for key, value in \
        self.__dict__.items())
        return f'{cls.__name__} ({representation})'
    
    cls.__repr__ = wrapper_mynewrapr
    
    return cls


@mynewrepr
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    

################################################################################
################################## OPERATIONS ##################################
################################################################################

p1 = Person('Josh', 23)

print(p1)