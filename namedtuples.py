from typing import NamedTuple


class Student(NamedTuple):
    """
    This is my first NamedTuple.

    I'll go to use  this NamedTuple to practice my skills.
    """
    NAME: str | None = None
    AGE: int | None = None
    HEIGHT: float | None = None
    WEIGHT: float | None = None
    EMAIL: str | None = None

    def print_tuple(self):
        return print(self)


a1 = Student('Malcon', 16, 1.75, 68, 'malcon@yahoo.com.br')

print(a1.AGE)


