class RegistrarChamadas:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with open(self.nome_arquivo, 'a') as f:
                f.write(f"Chamando a função {func.__name__} com argumentos: {args}, {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper

@RegistrarChamadas("registro.txt")
def minha_funcao(x, y):
    return x + y

minha_funcao(2, 3)