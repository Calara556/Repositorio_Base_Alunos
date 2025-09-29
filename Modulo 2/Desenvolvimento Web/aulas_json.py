"""import json
dados_json = '{"nome":"Maria Clara", "idade":15, "cidade":"Santana de Parnaíba"}'

dados_python = json.loads(dados_json)
print(dados_python["nome"])
print(dados_python["idade"])
print(dados_python["cidade"])"""

import json

pythonValue = {'Ischaracter': True, 'MiceCaught': 2, 'Name': 'Six', 'Age': 9 , 'HairColor': 'Black', 'IsGood': False, 'Friendships': 2, 'PeopleEaten': 2, 'Betrayal': 3, 'Riks': 8}
strinsOFJsonDATA = json.dumps(pythonValue)
print(strinsOFJsonDATA)