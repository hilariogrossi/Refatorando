class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0
    
    def ligar(self):
        if self.ligado:
            print(f'\nO carro {self.modelo} já está ligado. Nada acontece!\n')
        
        else:
            print(f'\nCarro {self.modelo} ligado!\n')
            self.ligado = True
    
    def desligar(self):
        if self.ligado:
            print(f'\nCarro {self.modelo} desligado!\n')
            self.ligado = False

        else:
            print(f'\nO carro {self.modelo} já está desligado. Nada acontece!\n')
    
    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f'\nA velocidade atual do {self.modelo} é {self.velocidade} Km/h.\n')
        
        else:
            print(f'\nNão é possível acelerar o carro {self.modelo} quando o mesmo está desligado!\n')
    
    def frear(self):
        if self.ligado:
            self.velocidade -= 10
            print(f'\nA velocidade atual do {self.modelo} é {self.velocidade} Km/h.\n')
        
        else:
            print(f'\nNão é possível frear o carro {self.modelo} qunado o mesmo está desligado!\n')

