from classe_animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome)
        self.raça = raça 

    def fazer_som(self):
        print(f"{self.nomr} está latindo: Au Au!")

    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo.")

animal1 = Cachorro('Bidu', 'Schnauzer')
animal1.comer()
animal1.abanar_rabo()