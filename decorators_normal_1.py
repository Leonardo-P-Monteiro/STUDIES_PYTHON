def decorador_externo(funcao):
    def wrapper():
        print("Decorador externo: antes")
        funcao()
        print("Decorador externo: depois")
    return wrapper

def decorador_interno(funcao):
    def wrapper():
        print("Decorador interno: antes")
        funcao()
        print("Decorador interno: depois")
    return wrapper

@decorador_externo
@decorador_interno
def minha_funcao():
    print("Função principal")

minha_funcao()