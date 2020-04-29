import pytest

from api.client import AlaskaClient


@pytest.fixture(scope="session")
def client():
    client = AlaskaClient("http://127.0.0.1:8091")
    return client