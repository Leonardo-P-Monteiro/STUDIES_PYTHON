"""
Vamos utilizar para nosso desafio:
 - listas contendo dicionários;
 - while para realizar as iterações;
 - enumarate().

Passos do desenvolvimento do game.
 - Criar uma tupla de dicionários que conterá as perguntas;
 - Criar laço de iteração while: para girar os acessos das perguntas e coletas
   das respostas.
 - Laço for para iterar sobre a lista e trazer o dicionário a ser trabalhado.
 - Acessar os itens do dicionários para exibilos em uma estrutura inteligível.
 - Coletar a resposta correta indicada pelo user.
 - Exibir placar de acertos e erros.

"""

questions_answers = (
    {
        'pergunta':'Qual a cor dos olhos verdes de Maria?',
        'alternativas': ['verdes', 'azuis', 'Castanhos'],
        'resposta': 0
     },

     {
        'pergunta':'O rei careca possui quantas tranças?',
        'alternativas': ['duas', 'três', 'nenhuma'],
        'resposta': 2
     },

     {
        'pergunta':'Quanto dos que não foram retornaram?',
        'alternativas': ['três', 'nenhum', '5'],
        'resposta': 1
     }
)



correct = 0
wrong = 0

for item_list in questions_answers:
    
    print(item_list.get('pergunta'))
    
    for index, alternative in enumerate(item_list['alternativas']):
        print(index,')', alternative)

    print('')
    
    answer_question = int(input('Informe uma das alternativas: '.strip()))
    
    analysis = True if item_list['resposta'] == answer_question \
    else False

    if analysis:
        correct +=1
        print('Parabéns! Você acertou.')
    
    else:
        wrong +=1
        print('Errou! Haha')

    print('')
    
    print(f'Placar: {correct=}, {wrong=}')
    
    print('')

print(f'Resultado final: {correct=}, {wrong=}')

print(f'Fim')