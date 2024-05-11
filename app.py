import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

# Indica o sucesso da requisição caso a resposta seja 200
if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json: # Percorre cada item nesse objeto, que representa um restaurante
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante: # Extrai dados específicos como o nome, o item, etc
            dados_restaurante[nome_restaurante] = []
        
        dados_restaurante[nome_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

# Cria um arquivo json para cada restaurante
for nome_restaurante, dados in dados_restaurante.items(): # Pegando somente os itens e não as informações
    nome_arquivo = f'{nome_restaurante}.json'
    # w é utilizado para escrever (write)
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4) # Cria o arquivo