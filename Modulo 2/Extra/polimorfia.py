from classe_animal import Animal
from animais_marinhos import AnimaisMarinhos
from classe_pássaro import Pássaro

# animal1 = Animal(23_000_000, "Megalodonte", 18.00, "Rei dos mares")
animal1 = Animal(23_000_000, "Megalodonte", 18.00, "Rei dos mares")
animal2 = AnimaisMarinhos(true, true, "Peixe_Piranha", "Prateado" "m")
animal3 = Pássaro('Coruja', 'Edwiges')

def comunicar(qualquer_animal):
    print(f"Tentando comunicação com {qualquer_animal.espécie}")
    qualquer_animal.fazer_som()

print("-"*50)
comunicar(animal1)

print("-"*50)
comunicar(animal2)

print("-"*50)
comunicar(animal3)