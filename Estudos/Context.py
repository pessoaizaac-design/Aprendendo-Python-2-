# Context Managers
from contextlib import contextmanager

class Adicionar:    
    def __init__(self):
        self.add = []

        
    def adicionar(self, item):
        self.add.append(item)
        print(f'{item} adicionado!')

@contextmanager
def Transacao():
    print("Inicializando a transação...")
    objeto = Adicionar()

    try:
        yield objeto
        print('Transação confirmada!')
    except Exception:
        print("Transação cancelada!")

with Transacao() as transacao:
    transacao.adicionar("Python")
    transacao.adicionar("Django")
