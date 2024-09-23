class MyDecoratorClass:
    
    def __init__(self, func_):
        self.func = func_

    def __call__(self, *args, **kwargs):
        execute = self.func(*args, **kwargs)
        return execute * 2

@MyDecoratorClass
def sum_(x, y):
    return x + y
###############################################################
var1 = sum_(1, 1)
print(var1)

