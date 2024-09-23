def zipper(list1, list2):

    list_1_zipper = list1
    list_2_zipper = list2
    new_list = []
    counter = 0

    if len(list1) < len(list2):
        while counter < len(list1):
            new_list.append((list1[counter], list2[counter]))
            counter += 1

    else:
        while counter < len(list2):
            new_list.append((list2[counter], list1[counter]))
            counter += 1

    return new_list


list_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(list_1,list_2))