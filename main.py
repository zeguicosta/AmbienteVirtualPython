from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_wolrd():
    '''
    Endpoint que exibe uma mensagem incrível!
    '''
    return {'Hello':'World!'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes!
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    # Indica o sucesso da requisição caso a resposta seja 200
    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {'Dados: ':dados_json}

        dados_restaurante = []
        for item in dados_json: # Percorre cada item nesse objeto, que representa um restaurante
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}