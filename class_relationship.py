class Car:
    
    def __init__(self, name):
        self.__name = name
        self.__motor = None
        self.__assembler = None


    @property # Getter on mode pythonic.
    def name(self):
        return self.__name
    
    @name.setter # Setter on mode pythonic.
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, new_motor):
        self.__motor = new_motor

    @property
    def assembler(self):
        return self.__assembler
    
    @assembler.setter
    def assembler(self, new_assembler):
        self.__assembler = new_assembler

class Motor(Car):

    def __init__(self, name):
        self.__name = name

    def get_name(self): # Getter on classic mode.
        return self.__name
    
    def set_name(self, new_motor): # Setter on classic mode.
        self.__name = new_motor


class Assembler:
    
    def __init__(self, name):
        self.__name = name

    def get_name(self): # Getter on classic mode.
        return self.__name
    
    def set_name(self, new_motor): # Setter on classic mode.
        self.__name = new_motor

################################################################################
################################## OPERATIONS ##################################
################################################################################

c1 = Car('Veraneio')
a1 = Assembler('GM')
m1 = Motor('Diesel')

c1.motor = m1  # Here is doing an aggregation of objects.
c1.assembler = a1 # Here is doing an aggregation of objects.



print('Car: ', c1.name)
print("#"*10)
print( 'Motor: ', c1.motor.get_name())
print("#"*10)
print('Assembler: ', c1.assembler.get_name())

