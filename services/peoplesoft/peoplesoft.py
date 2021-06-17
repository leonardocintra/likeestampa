import requests
import json

BASE_URL = 'https://people-stage.herokuapp.com/v1/peoplesoft'

HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


def cadastrar_cliente(cliente):
    cliente_existe = buscar_cliente_by_cpf(cliente['cpf'])

    if cliente_existe:
        return cliente_existe['records'][0]['id']
        # TODO: verificar tambem se o endereco ainda eh o mesmo

    data = {
        'nome': cliente['nome'],
        'cpf': cliente['cpf'],
        'sexo': 'M',
        'email': cliente['email'],
        'enderecos': [
            {
                'cep': cliente['cep'],
                'endereco': cliente['endereco'],
                'numero': cliente['numero'],
                'bairro': cliente['bairro'],
                'cidade': cliente['cidade'],
                'uf': cliente['uf'],
                'referencia': cliente['referencia'],
                'complemento': cliente['complemento'],
            }
        ]
    }

    response = requests.post(BASE_URL + '/pessoa',
                             data=json.dumps(data), headers=HEADERS)

    cliente_json = json.loads(response.text)

    if response.status_code == 201:
        return cliente_json['records'][0]['id']
    elif response.status_code == 409:
        cliente_json = buscar_cliente_by_id(cliente['id'])
        return cliente_json['records'][0]['id']
    else:
        print(response.text)
        # TODO: Enviar erro no telegram


def buscar_cliente_by_cpf(cpf):
    response = requests.get(BASE_URL + '/pessoa/cpf/' + cpf, headers=HEADERS)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(response.text)


def buscar_cliente_by_id(id):
    response = requests.get(BASE_URL + '/pessoa/' + id, headers=HEADERS)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(response.text)