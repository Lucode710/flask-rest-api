import pytest
from src import create_app
from src.api import Api
from src.exceptions import *

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True
    })
    Api(app)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_list_prizes_no_filters(client):
    response = client.get('/api/catalogs/1/prizes')
    assert response.status_code == 200
    data = response.get_json()
    assert 'total' in data
    assert 'prizes' in data
    assert data['total'] == len(data['prizes'])

def test_list_prizes_with_filter(client):
    response = client.get('/api/catalogs/1/prizes?filter={"id":1}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total'] == 1
    assert data['prizes'][0]['id'] == 1

def test_list_prizes_with_pagination(client):
    response = client.get('/api/catalogs/1/prizes?pagination={"page":1,"per_page":2}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total'] == 2
    assert len(data['prizes']) == 2

def test_list_prizes_with_filter_and_pagination(client):
    response = client.get('/api/catalogs/1/prizes?filter={"description":"desc"}&pagination={"page":1,"per_page":3}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total'] == 3

    assert len(data['prizes']) == 3
def test_list_prizes_ivalid_input_with_filter_and_pagination(client):
    response = client.get('/api/catalogs/1/prizes?filter={"description":"desc"}&pagination={"pag":1,"per_page":3}')
    assert response.status_code == 400
    data = response.get_json()
    assert data['title'] == 'Invalid API Usage'

def test_list_prizes_invalid_catalog(client):
    response = client.get('/api/catalogs/999/prizes')
    assert response.status_code == 404
    data = response.get_json()
    assert data['title'] == 'Catalog Not Found'

def test_list_prizes_invalid_filter_format(client):
    response = client.get('/api/catalogs/1/prizes?filter=invalid')
    assert response.status_code == 400
    data = response.get_json()
    assert data['title'] == 'Input Query Not Valid'

def test_list_prizes_invalid_pagination_format(client):
    response = client.get('/api/catalogs/1/prizes?pagination=invalid')
    assert response.status_code == 400
    data = response.get_json()
    assert data['title'] == 'Input Query Not Valid'

def test_list_prizes_invalid_method(client):
    response = client.post('/api/catalogs/1/prizes')
    assert response.status_code == 405
    data = response.get_json()
    assert data['title'] == 'Methon Not Allowed'