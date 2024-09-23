class FirstErro(Exception): # Aqui criamos o nosso erro herdando a partir da superclasse Exception.
    ...

class SecondErro(Exception):
    ...

def my_error_rise(num): # Essa função estamos fazendo apenas para levantar uma possibilidade do nosso erro.
    
    if num >= 0:
        my_exception = FirstErro('The variable "num" is bigger than or equal zero(0).')
        my_exception.add_note('This is one note that i insert.') # Aqui você pode perceber que conseguimos adicionar notas aos erros.
        # o que pode ser útil em situações em que queremos salvar atributos, dados, variáveis e etc, para consulta e análise do erro.
        my_exception.add_note('This the second note.')
        raise my_exception
    
    return 'Atribute provided.'



try:
    my_error_rise(9)

except FirstErro as e:
    print('Name of erro: ', e.__class__.__name__)
    print('Text of erro: ', e)
    e.add_note('Note added on exception scope.')
    print('List of notes of erros: ', e.__notes__)
    exception_from_except = SecondErro('This is our second erro.')
    exception_from_except.add_note('Note the second exception.')
    raise exception_from_except from e # Aqui estamos levantando uma segunda exceção
# dentro do bloco except. 
    




