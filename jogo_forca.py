secret_word = 'soccer'
correct_letter = ''
counter = 0

while True:

    letter_provide = input('Provide a letter: ')
    counter += 1

    if len(letter_provide) > 1:
        print('You give more than one letter. Please, supply again.')
        continue

    if letter_provide in secret_word:
        correct_letter += letter_provide

    constructed_word = ''
    for each_letter in secret_word:
        if each_letter in correct_letter:
            constructed_word += each_letter
        
        else:
            constructed_word += '*'
    
    if constructed_word == secret_word:
        print('Congratulations! You win!')
        print(f'The word formed is:  {constructed_word}')
        print(f'You tried {counter} times until win.')
        break
    else:
        print(constructed_word)
