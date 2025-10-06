class AnimaisMarinhos():
    def __init__(self, espécie, tem_nadadeira, tem_brânquias, cores, sexo):
        self.tem_nadadeira = tem_nadadeira 
        self.tem_brânquias= tem_brânquias
        self.espécie = espécie
        self.cores = cores
        self.sexo = sexo

    def nadar(self):
        return print(f'Sou um {self.espécie} nadando do mar 🌊')
    
    def comer(self):
        return print('comendo algumas: algas...')
        
    
"""pássaro1 = Pássaro(0.14, ['Marrom', 'Branco', 'Cinza'], 'Pardal', 'M')
pássaro1.cantar()"""