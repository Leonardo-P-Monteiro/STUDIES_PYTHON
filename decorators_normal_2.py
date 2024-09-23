# def maiusculo(funcao):
#     def wrapper():
#         print('maiusculo')
#         return funcao().upper()
#     return wrapper

# def negrito(funcao):
#     def wrapper():
#         print('negrito')
#         return f"**{funcao()}**"
#     return wrapper

# @maiusculo
# @negrito
# def minha_funcao():
#     return "olá, mundo"

# resultado = minha_funcao
# print(resultado())


def decorador1(funcao):
    print('Dec_1 - Sou o segundo a ser aplicado.')
    def wrapper():
        print("Decorador 1: Antes")
        funcao()
        print("Decorador 1: Depois")
    return wrapper

def decorador2(funcao):
    print('Dec_2 - Sou o primeiro a ser aplicado.')
    def wrapper():
        print("Decorador 2: Antes")
        funcao()
        print("Decorador 2: Depois")
    return wrapper

@decorador1
@decorador2
def minha_funcao():
    print("Minha função")

minha_funcao()