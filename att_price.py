from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = deepcopy(produtos)

produtos_atualizados = deepcopy([
    {**p, 'preco': round(p['preco']*1.1, 2)} 
    for p in novos_produtos
    ])

produtos_atualizados.sort(key= lambda p: p['nome'], \
                          reverse=True)

produtos_ordenados_nome = deepcopy(produtos_atualizados)

produtos_ordenados_preco = deepcopy(sorted(produtos_atualizados, key=lambda p: \
                                  p['preco']))

print( *produtos_ordenados_nome, '', *produtos_ordenados_preco, sep='\n')



