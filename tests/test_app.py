from fastapi.testclient import Testclient
from fastapi_zero.app import app

client = Testclient(app)
