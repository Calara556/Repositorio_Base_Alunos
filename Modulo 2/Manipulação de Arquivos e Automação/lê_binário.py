def lê_binário():
    try:
        with open("binary.jpg" ,"r") as fs1:
            dados = fs1.read()
        with open("cópia.arquivo.txt" ,"w") as fs2:
            fs2.write(dados)
        with open("cópia.arquivo.txt" ,"w") as fs2:
            fs2.write(dados)
        with open("cópia.arquivo.txt" ,"w") as fs2:
            fs2.write(dados)
    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
        arquivo = open("arquivo.txt", "W")
        arquivo.write("Algo dentro!")
        arquivo.close()
    except IOError as e:
        print('Deu algo errado @_@') 
    print("OK! ~_~")
lê_binário()

