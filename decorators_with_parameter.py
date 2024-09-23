def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            print(nome)
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        
        return sua_nova_funcao
    
    return decorador

# @parametros_decorador(nome='5')
# @parametros_decorador(nome='4')
# @parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y
#######################################################################
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)









# soma_c_1_no_final = parametros_decorador('1')(soma)
# soma_c_2_no_final = parametros_decorador('2')(soma_c_1_no_final)
# print(dec(1,1))
# print(soma_c_2_no_final(1,1))