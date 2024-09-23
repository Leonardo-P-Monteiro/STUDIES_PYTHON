dict_1 = {
    'nome':'João',
    'sobrenome': 'Epaminondas',
    'Idade': 35,
}

# print(dict_1.setdefault('Endereço', 'Rua das Flores'))
# print(dict_1.setdefault('Carro'))
# print(dict_1)

# print(dict_1)

dicionario1 = {'nome': 'João'}
dicionario2 = {'informacoes_adicionais': {'altura': 1.80, 'peso': 75}}
# dicionario1.update(dicionario2)  # type: ignore
# print(dicionario1)

for i, (x,y) in enumerate(dict_1.items()):
    print(f'chave: {x=} Valor: {y=}')


