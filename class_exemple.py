class Pessoa:
    var1= 'Léo'
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def action(self, num1, num2):
        return (num1 + num2)

pessoa1 = Pessoa("Alice", 30)

print(pessoa1.__dict__)  # Saída: {'nome': 'Alice', 'idade': 30}
print(Pessoa.__dict__)