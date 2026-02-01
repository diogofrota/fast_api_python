from http import HTTPStatus
from fastapi.testclient import Testclient
from fastapi_zero.app import app

client = Testclient(app)

response = client.get('/')

assert response.json() == {'message': 'Olá mundo'}
assert response.status_code == HTTPStatus.OK
