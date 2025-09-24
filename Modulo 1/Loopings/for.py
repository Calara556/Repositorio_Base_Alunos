"""L=[8,9,15]
for e in L:
    print(e)"""

"""L=["lotús", "lírio", "dama-da-noite", "papoula", "tulípa", "margarida", "ipê", "hibisco", "flor-de-lis", "peônia"]
for s in L:
    for letra in s:
        print(letra)"""

"""def exibe_maior():
    L=[1,7,2,4]
    máximo=L[0]
    for e in L:
        if e > máximo: 
            máximo = e
    print(máximo)"""

"""def exibe_menor():
    L=[1,7,2,4]
    mínimo=L[0]
    for e in L:
        if e < mínimo:
            mínimo = e
    print(mínimo)"""

"""def range_exercicio():
    for v in range(10):
        print(v)"""

"""def exercicio_de_range():
    for v in range(5, 8):
        print(v)"""

"""def range_salto():
    for t in range(3,33,3):
        print(t, end=" ")
range_salto()"""


nome = "Maria Clara"
idade = 15
grana = 24.60
print("%s tem %d e R$%f no bolso." % (nome, idade, grana))