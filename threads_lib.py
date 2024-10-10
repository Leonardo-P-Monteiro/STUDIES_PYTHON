import threading
from time import sleep

def counter_(number):
    for i in range(1, number +1):
        print(i)
        sleep(1)


class ThreadInClass(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.lock = threading.Lock()
    
    def run(self):
        for i in range(1, self.number + 1):
            print(i)
            sleep(1)

# Thread with locks.
class Stock(threading.Thread):
    def __init__(self, stock_tickets: int):
        self.stock_ticket = stock_tickets
        # Cadeado da tread para que ela não dê erro de processamento simultâneo.
        # Assim cada tread vai ser processada uma por vez.
        self.lock = threading.Lock()
    
    def buy(self, tickets: int):
        # trancando os recursos para serem "consumidos" um por vez pelas treads.
        self.lock.acquire()

        if self.stock_ticket < tickets:
            print('Não há estoque suficiente')
            # Liberando os recursos para a próxima tread.
            self.lock.release()
            return

        sleep(1)

        self.stock_ticket -= tickets
        print(f'Você comprou {tickets}. Ainda temos em estoque \
              {self.stock_ticket} em estoque.')

        # Liberando os recursos para a próxima tread.
        self.lock.release()       


################################################################################



# Utilizando uma classe que herda de Tread.

tread_class_test = ThreadInClass(10)
tread_class_test.start()
tread_class_test.join() # isso aqui faz com que o script espere esse processo terminar para dar continuidade do restante.
print(f'Tread {tread_class_test.__class__.__name__} terminou e o código vai \
continuar a ser executado agora.')

# Usando uma função alvo.
t1 = threading.Thread(target=counter_, args=(5,))
t1.start()
print('Tread através de função target terminou.')

# 
ingressos = Stock(10)

for i in range(1, 15):
    t = threading.Thread(target=ingressos.buy, args= (1,))
    t.start()