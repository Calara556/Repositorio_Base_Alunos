from classe_animal import Animal

class Gato(Animal):

    def fazer_som(self):
        print(f"{self.nome} está miando: Miau!")

animal2 = Gato("frajola")
animal2.fazer_som()