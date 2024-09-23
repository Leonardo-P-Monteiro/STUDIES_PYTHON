"""
Etapas do algorítimo:
- Vamos construir um laço de iteração que vai acessar lista por lista
  para que possamos manipulá-las.
- Lançaremos os itens das listas dentro de um set().
- Vamos fazer um laço de iteração para conferir cada item da lista dentro
  do set() e descobrir se é duplicado.
- Sendo duplicado, lançaremos em um novo set() os duplicados. 
- Sendo o set() de duplicados vazio, remeteremos -1 como resultado.
"""

list_list_int = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# for item_list_int in list_list_int:
#     item_list_int_set = set(item_list_int)
#     item_list_int_duble = list()

#     for x in item_list_int_set:
#         if item_list_int.count(x) >= 2:
#             item_list_int_duble.append(x)

#     if not item_list_int_duble:
#         print('-1')
#     else:
#         print(item_list_int_duble)
    
    # Não conferi, mas o código ficou diferente das etapas do algorítimo.

def first_duplicate(interator):
    verify_numbers = set()
    first_dupli_num = -1

    for inter_list in interator:

        if inter_list in verify_numbers:
            first_dupli_num = inter_list
            break

        verify_numbers.add(inter_list)
        
       
    
    return first_dupli_num

for i in list_list_int:
    print(first_duplicate(i))