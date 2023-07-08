import requests
import json

# Configurações do Zabbix
url = 'http://seu_zabbix/api_jsonrpc.php'
user = 'usuario'
password = 'senha'

# Função para fazer uma requisição à API do Zabbix
def make_request(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()

# Função para fazer login e obter o token de autenticação
def login():
    data = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user': user,
            'password': password
        },
        'id': 1
    }
    response = make_request(data)
    return response['result']

# Função para exportar todos os hosts
def export_hosts(token):
    data = {
        'jsonrpc': '2.0',
        'method': 'host.get',
        'params': {
            'output': 'extend'
        },
        'auth': token,
        'id': 1
    }
    response = make_request(data)
    return response['result']

# Faz login e obtém o token de autenticação
token = login()

# Exporta todos os hosts
hosts = export_hosts(token)

# Exibe os hosts exportados
for host in hosts:
    print(host)
