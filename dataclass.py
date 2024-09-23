from dataclasses import dataclass, asdict, astuple

@dataclass
class Person:
    name: str | None 
    surname: str | None 
    height: float | None = None
    weight: float | None = None
    address: str | None = None
    _email: str | None = None

    def __post_init__(self):  # It is optional. It's doesn't mandatory.
        print(f'Hi! My name is {self.name}')
        

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self.email = email
        return self.email



p1 = Person('Kamala', 'Harrys', 65.9, 1.68, 'Street, J', 'kh@gmail.com')
print(p1.email)
print('*'*9)
print('asdict: ', asdict(p1))
print('*'*9)
print('astuple: ', astuple(p1))