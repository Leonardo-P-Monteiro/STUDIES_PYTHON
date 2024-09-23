################################################################################
########################### DECORATORS WITH CLASSES ############################
################################################################################

# DECORATOR CLASS
def mynewrepr(cls):
    
    def wrapper_mynewrapr(self):
        representation = ', '.join(f'{key}: {value!r}' for key, value in \
        self.__dict__.items())
        return f'{cls.__name__} ({representation})'
    
    cls.__repr__ = wrapper_mynewrapr
    
    return cls

# DECORATOR METHOD
def new_speak_name(method):
    def wrapper_skpeak_name(self, *args, **kwargs):
        exit_value = method(self, *args, **kwargs)

        if 'Josh'.lower() in exit_value.lower():
            return 'Nice to see you again, Jhosh!'
        else:
            return exit_value
    
    return wrapper_skpeak_name


@mynewrepr
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @new_speak_name
    def speak_name(self):
        return f'You are {self.name}'
    

################################################################################
################################## OPERATIONS ##################################
################################################################################

p1 = Person('Josh', 23)
p2 = Person('Ellie', 23)

print(p1.speak_name())
print(p2.speak_name())