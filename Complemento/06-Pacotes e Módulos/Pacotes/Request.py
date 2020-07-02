import requests


def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/22041001/json/')
    print(response.status_code)
    print(response.json())

    dados_cep = response.json()
    print(dados_cep['logradouro'])

    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    return response.json()


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    retorna_dados_cep('22041001')
    print(retorna_dados_pokemon('pikachu'))
    print(retorna_response('https://globallabs.academy/'))
