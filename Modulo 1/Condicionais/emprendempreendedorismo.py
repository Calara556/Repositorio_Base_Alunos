estoque = {"Cappucino": [ 1000, 2.30],
         "Espresso": [ 500, 0.45],
         "Latte": [ 2001, 1.20],
         "Americano": [ 100, 1.50],
         "Mocha": [ 800, 6.50],
         "Latte Macchiato": [ 300, 10.0 ],
         "Macchiato": [3000, 17.99],
         "Mochaccino": [ 90, 9.50],
         "Espresso tônica": [20, 17.0],
         "Frappucino": [30, 20.50],
         "Café com leite vegetal": [40, 16.0],
         "Pumpikin Spice Latte": [12, 18.50],
         "Affogato": [15, 16.99],
         "Espresso duplo": [3, 9.0],
         "Café com mel": [ 2, 13.50],
         "Café coado": [2, 8.0],
         "Bolo de cenoura": [2000, 10.0],
         "Bolo de coco gelado": [100, 19.50],
         "Pão de queijo": [900, 9.99],
         "Brownie": [400, 8.00]}
produto = input("Digite o produto selecionado: ")
quantidade = int(input("Digite o quantidade: "))
venda = [ [produto, quantidade] ]
total = 0
if produto in estoque:
  print("Vendas:\n")
  for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
else:
    print("Não temos este produto no estoque!")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])