class Funcionario:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def mostrar_dados(self):
        print(f'Nome: {self.name}')
        print(f'Salário: {self.cash}')
    
class Gerente(Funcionario):
    def __init__(self, name, cash, bonus):
        super().__init__(name, cash)
        self.bonus = bonus

    def mostrar_dados(self):
        print(f'Nome: {self.name}')
        print(f'Salário: {self.cash} R$')
        print(f'Bônus: {self.bonus} R$')

class Programador(Funcionario):
    def __init__(self, name, cash, ling):
       super().__init__(name, cash)
       self.ling = ling

    def mostrar_dados(self):
        print(f'Nome: {self.name}')
        print(f'Salário: {self.cash} R$')
        print(f'Linguagem: {self.ling}')

gerente = Gerente("Carlos", 5000, 1000)
programador = Programador("Higor", 4000, "Python")

gerente.mostrar_dados()
programador.mostrar_dados()
