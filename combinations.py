from itertools import product, permutations, combinations

l1 = ['Camisa', 'Bermuda', 'Calça']
l2 = ['azul', 'vermelho', 'marrom', 'violeta']
l3 = ['p', 'm', 'g']
l4 = ('M', 'F')


product_v = product(l1, l2) # Vai me retornar todas as COMBINAÇÕES possíveis a
# partir da junção de dois iteráveis. 
permutations_v = permutations(l1) # Vai me retornar todas ORDENAÇÔES possíveis de
# serem feitas naquele iterável.
combinations_v = combinations(l1, r= 2) # Aqui vai me retornar todas as COMBINAÇÔES
# possíveis de serem feitas com esse iterável.

print(*list(product_v), sep= '\n')
print('-'*10)
print(*list(permutations_v), sep= '\n')
print('-'*10)
print(*list(combinations_v), sep= '\n')

