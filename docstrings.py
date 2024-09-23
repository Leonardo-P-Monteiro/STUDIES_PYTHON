class Person:
    """ This is class Person.

    I create this class only to practice my skills with "docstrings". 

    This text will be showing on the response of help function. 
    """
    def __init__(self, name: str, age:int|None =None, weight:float|None=None, \
                 height:float|None = None):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def say_hello(self) -> None:
        """Method "say_hello".

        This method make the instance say "hello".

        It return a print of the phrase "hello".
        """
        return print(f'Hi! My name is {self.name}!')

def answer_person() -> None:
    """ This class is called the "answer_person". 

    This is an example how to use docstring in functions.
    """
    return print('Nice to meet you!')



# p1 = Person('Oliver', 27, 83, 1.98)
# answer_ = answer_person

# p1.say_hello()
# answer_()
help(Person)
help(answer_person)