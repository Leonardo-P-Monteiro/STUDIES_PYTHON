from abc import ABC, abstractmethod
import math

################################# DATA BANK ####################################

b_clientes = []
b_contas = []

############################## ABSTRACT CLASSES ################################
class Conta(ABC):

    def __init__(self, agencia, num_cont, saldo):
        self._agencia = agencia
        self._num_cont = num_cont
        self._saldo = saldo
        b_contas.append(self)
    
    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, new_agenc):
        self._agencia = new_agenc
    
    @property
    def num_cont(self):
        return self._num_cont

    @num_cont.setter
    def num_cont(self, new_num_cont):
        self._num_cont = new_num_cont
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
    
    @abstractmethod
    def sacar(self):
        pass
    
    def deposito(self, valor):
        self.saldo += valor
        self.detalhes(f'Novo Saldo: {self.saldo}')
    
    def detalhes(self, msg):
        print(msg)
    
    def __repr__(self):
        class_name = self.__class__.__name__
        attr = f'({self._agencia}, {self._num_cont}, {self._saldo})'
        return f'{class_name}{attr}'

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        b_clientes.append(self)
        
    def __repr__(self):
        class_name = self.__class__.__name__
        attr = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attr}'



################################### CLASSES ####################################

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta: Conta | None = None

class Banco:
    def __init__(self, cliente: list[Pessoa]|None = None, conta: list[Conta]|None = None,\
                  agencia:list[int]|None = None):
        self.clientes = cliente or []
        self.contas = conta or []
        self.agencias: Conta | list = agencia or []
    
    def _checa_agencia(self, conta:Conta):
        if conta.agencia in self.agencias:
            print(f'Agência pertence ao banco: {conta.agencia}')
            return True
        else:
            print(f'Agência não pertence ao banco: {conta.agencia}')
            return False
    
    def _checa_cliente(self, cliente:Pessoa):
        if cliente in self.clientes:
            print(f'Cliente pertence ao banco.')
            return True
        else:
            print(f'Cliente não pertence ao banco.')
            return False
        
    def _checa_conta(self, conta:Conta):
        if conta in self.contas:
            print(f'Conta pertence ao banco.')
            return True
        else:
            print(f'Conta não pertence ao banco.')
            return False
    
    def _checar_conta_cliente(self, cliente:Cliente, conta):
        if conta in cliente.conta:
            print('Esta conta pertence a esse cliente.')
            return True
        else:
            print('Esta conta não pertence a esse cliente.')
            return False
    
    def __repr__(self):
        class_name = self.__class__.__name__
        attr = f'({self.agencias!r}, {self.contas}, {self.clientes})'
        return f'{class_name}{attr}'

    def autenticar(self, cliente: Cliente, conta:Conta):
        return self._checa_conta(conta) and \
        self._checa_agencia(conta) and \
        self._checar_conta_cliente(cliente, conta) and \
        self._checa_cliente(cliente)

class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        pos_saque = self.saldo - valor
        if pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Novo Saldo: {self.saldo}')
            return self.saldo
        else:
            return self.detalhes('Saldo insuficiente.')

class ContaCorrente(Conta):

    def __init__(self, agencia, num_cont, saldo, limite:float):
        super().__init__(agencia, num_cont, saldo)
        self.limite_cc = limite


    def sacar(self, valor):
        pos_saque = self.saldo - valor
        limite_max = self.limite_cc
        

        if pos_saque >= limite_max:
            self.saldo -= valor
            self.detalhes(f'Novo Saldo {self.saldo}')
            return
        else:
            self.detalhes(f'Você atingiu seu limite. Saldo atual: {self.saldo}')
        


    


    






################################################################################
################################## OPERATIONS ##################################
################################################################################



cp1 = ContaPoupanca(1, 1, 100) # Poupanças estão funcionando normalmente.
cc1 = ContaCorrente(3, 1, 100, -100) # Correntes estão funcionando normalmente.
c1 = Cliente('Biden', 92)
b1 = Banco()


print(c1)
print(cc1)
# cont_poup1.deposito(100)
# cont_poup1.sacar(200)

# cont_corr1.deposito(100)
# cont_corr1.sacar(200)
# cont_corr1.sacar(98)


if Banco.autenticar(b1, c1, cc1):
    cc1.deposito(100)
    