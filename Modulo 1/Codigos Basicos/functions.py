"""texto_escrito="Este livro é legal!"
outro_texto='vou aprender a programar'
texto=
"""
#primeira linha
#segunda linha
#terceira linha
"""
print(texto)
print("\tOi!\nEu me chamo\"(Maria Clara)\"!!!")
outro_texto=texto_escrito
print(outro_texto)
bolos_subtraidos = 50
pedaços_bolos = 190
pedaços_bolos -= bolos_subtraidos
print(pedaços_bolos)
pirulitos_subtraidos = 30
quantidade_pirulitos = 1000
quantidade_pirulitos += pirulitos_subtraidos
print(quantidade_pirulitos)
pacotes_doritos = 10
quantidades_subtraidas = 66
pacotes_doritos /= quantidades_subtraidas
print(pacotes_doritos)
carteira_digital = 0
print(carteira_digital)
carteira_digital += 100
print(carteira_digital)
carteira_digital -= 75.99
print(carteira_digital)
carteira_digital += 200
print(carteira_digital)
def dizer_ola( nome_usuario="Geovanna"):
    print("olá", nome_usuario)
dizer_ola("Maria Clara")
dizer_ola("Leão")
dizer_ola()
dizer_ola(1900)
dizer_ola(100*4)
"""
"""nome = input("insira um numero: ")
resultado = nome - 2
print(resultado)
numero_string = int(input("insira um numero: "))
resultado = nome - 2
print(resultado)
"""
"""numero = 3
def apresentar_numero():    
    numero = 2
    print(numero)

apresentar_numero()
print(numero)
numero = 30
def apresentar_numero():
    global numero
    print(numero)
    numero=7
    print(numero)

apresentar_numero()
print(numero)
"""
def quadrado(area):    
    resultado = area ** 2
    return resultado
print(quadrado(4))

def salario(valor):
    resultado = valor + valor * 0.15
    return resultado
print(salario(1000))

def triangulo(base, altura):
    resultado = base * altura / 2
    return resultado
print(triangulo(6,9))

def conversor(celsius):
    fahrenheit = (9*celsius+160)/5
    return fahrenheit
print(conversor(100))

def valores(x,y):
    z=x
    x=y
    y=z
    return ("o valor de x é: ",x,
            "e o valor de y é: ", y)
print(valores(100, 40))

def paralelepipedo(base, altura, largura):
    resultado = base * altura * largura
    return resultado
print(paralelepipedo(6, 10, 20))

