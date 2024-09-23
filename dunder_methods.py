class Person:
    
    def __new__(cls, *args, **kwargs):
        print('We are constructing our instance of class.')
        instance = super().__new__(cls) # Here we are calling the constructor method of the instance.
        print('We constructed our instance of class.')
        return instance
        
    def __init__(self, name):
        print('Now, we are initializing the instance.')
        self.name = name
        print('Our class and our instance it\'s complete.')

class Points:

    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y
    
    def __repr__(self):
        return f'Point({self.point_x!r}, {self.point_y!r})'
    
    def __add__(self, other):
        self.point_x = self.point_x
        self.point_y = self.point_y
        other.point_x = other.point_x
        other.point_y = other.point_y

        new_point = f'Point({self.point_x + other.point_y}, {self.point_y + \
        other.point_y})'

        return new_point
    
    def __lt__(self, other):
        self.sum = self.point_x + self.point_y
        other.sum = other.point_x + other.point_y

        return self.sum < other.sum
    
    def __gt__(self, other):
        self.sum = self.point_x + self.point_y
        other.sum = other.point_x + other.point_y

        return self.sum > other.sum

################################################################################
################################## OPERATIONS ##################################
################################################################################

# p1 = Person('Heloise')
# print(p1.name)
point1 = Points(1, 2)
point2 = Points(3, 3)
point3 = point1 < point2
point4 = point1 > point2
print(f'{point1=} < {point2=} =', point3)
print(f'{point1=} > {point2=} =', point4)