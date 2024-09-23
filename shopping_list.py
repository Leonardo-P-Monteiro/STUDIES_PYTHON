shopping_list = []


while True:
    choice = input('Choice an option \n[a]dd [e]xclude [l]ist: ').upper().\
        strip()
    
    if len(choice) > 1:
        print('Your choice it\'s wrong. Please, write with one \
character again.')

    elif choice == 'A':
        new_item = input('Provide an item: ').strip().capitalize()
        shopping_list.append(new_item)
        
    elif choice == 'L':
        if not shopping_list:
            print('List empty.')
        
        for index, item in enumerate(shopping_list):
            print(index+1, item)

    elif choice =='E':
        index_item = input('Provide an index: ').strip()
        
        try:
            index_int = int(index_item)
            index_int -= 1
            if index_int > len(shopping_list) or index_int < 0:
                print('There is not this index on the list.')
                continue
            
            shopping_list.pop(index_int)

        except ValueError:
            print('Erro unknow.')
            
    else:
        print('Write an answer listed.')
