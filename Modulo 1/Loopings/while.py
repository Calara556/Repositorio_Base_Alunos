"""def exercicio_1():
x = 1
while x <=50000:
    print(x)
    x = x + 1"""

"""def exercicio_2():
x = 50
while x <= 100:
    print(x)
    x = x + 1"""

"""def exercicio_3():
    x = 10
    while x >=0:
        print(x)
        x = x - 1
    print('FOGO!!')
exercicio_3()"""

"""def numeros_pares():
    fim=int(input("Digite o último número a imprimir:"))
    x = 0 
    while x <= fim:
        if x % 2 == 0:
            print(x) 
        x = x + 1
numeros_pares()"""

"""def numeros_impares():
    fim=int(input("Digite o último número a imprimir:"))
    x = 0
    while x <= fim:
        if x % 2 == 1:
            print(x)
        x = x + 1
numeros_impares()"""

def arvore_de_natal():
    linha = 1
    while linha <= 10:
        coluna = 1
        while coluna <= linha:
            print('💚', end="")
            print('❤️', end="")
            print('💛', end="")
            coluna = coluna + 2
        print ()
        linha = linha + 1
arvore_de_natal()
