from itertools import groupby

pessoas = [
    {'nome': 'Alice', 'idade': 30},
    {'nome': 'Bob', 'idade': 25},
    {'nome': 'Charlie', 'idade': 30},
]

pessoas.sort(key= lambda a: a['idade']) # inserido por mim pois daria erro caso
#não houvesse.

def por_idade(pessoa):
    return pessoa['idade']

for idade, grupo in groupby(pessoas, key=por_idade):
    print(f"Idade: {idade}")
    for pessoa in grupo:
        print(f"  {pessoa['nome']}")

# RESULTADO:
# Idade: 25
#   Bob    
# Idade: 30
#   Alice  
#   Charlie