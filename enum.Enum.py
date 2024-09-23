# CÓDIGO NÃO FOI DESENVOLVIDO POR MIM - VIA IA. 


from enum import Enum

class StatusPedido(Enum):
    RECEBIDO = "Recebido"
    EM_PREPARO = "Em Preparo"
    PRONTO = "Pronto para Retirada"
    ENTREGUE = "Entregue"

def processar_pedido(pedido):
    if pedido.status == StatusPedido.RECEBIDO:
        print("Pedido recebido, iniciando o preparo...")
        # ... lógica para processar o pedido
        pedido.status = StatusPedido.EM_PREPARO
    elif pedido.status == StatusPedido.EM_PREPARO:
        print("Pedido em preparo...")
        # ... lógica para continuar o preparo do pedido
        pedido.status = StatusPedido.PRONTO
    # ... outras lógicas para os demais status

class Pedido:
    def __init__(self, itens):
        self.itens = itens
        self.status = StatusPedido.RECEBIDO  # Inicializa o status como "Recebido"

# Criando um pedido
meu_pedido = Pedido(["Pizza", "Refrigerante"])

# Processando o pedido
processar_pedido(meu_pedido)
print(meu_pedido.status)  # Saída: StatusPedido.EM_PREPARO