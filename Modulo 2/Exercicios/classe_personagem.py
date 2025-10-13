class Personagem():

    def __init__(self, nome, cor_do_cabelo, cor_do_olho, sexo, idade):
        self.nome = nome
        self.cor_do_cabelo = cor_do_cabelo
        self.cor_do_olho = cor_do_olho
        self.sexo = sexo
        self.idade = idade

    def dançar(self):
            return print(f'{self.nome} está dançando jazz')
        
    def dormir(self):
         return print(f'{self.nome} ficou cansada e foi dormir')

    def conversar(self):
         return print(f'{self.nome} está conversando com um funcionário da empresa')
    
    def chorar(self):
         return print(f'{self.nome} está senível demais e agora está chorando')
    
    def brincar (self):
         return print(f'{self.nome} respirou fundo e relaxou')
    
personagem1 = Personagem('Ha-yoon', 'Castanho', 'Mel', 'f', '15')
personagem1.dançar()

personagem2 = Personagem('Hwang', 'Castanho', 'Verde', 'm', '42')
personagem2.conversar()

personagem3 = Personagem('Mi-young', 'Preto', 'Mel', 'f', '39')
personagem3.chorar()

personagem4 = Personagem('Min-jun', 'Castanho', 'verde', 'm', '4')
personagem4.brincar()

personagem5 = Personagem('Yeo-jin', 'preto', 'mel', 'f', '19')
personagem5.dormir()