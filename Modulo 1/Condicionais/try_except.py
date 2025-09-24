"""try:
    divisão = 10 / 0
    print(divisão)
except:
    print('''Não foi possível realizar essa operação!!''')"""

def divide(x,y):
    try:
        resultado=x/y
    except ZeroDivisionError:
        print("Por favor, não utilize zeros!")
    except:
        print("\033[91m Algo deu errado...")
    else:
        print(f"Seu resultado é: {resultado}")
    finally:
        print("\033[92m Vamos fazer de novo?")
divide(13,9)