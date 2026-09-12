import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_index(client):
    """Testa se a página inicial renderiza corretamente."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Calculadora de Frete" in response.data

def test_post_calcular_sucesso(client):
    """Testa cálculo de frete com sucesso abaixo do limite."""
    response = client.post('/calcular', 
                           data=json.dumps({'valor_carrinho': 150.00, 'regiao': 'Sudeste'}),
                           content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['frete'] == 15.00
    assert data['regiao'] == 'Sudeste'

def test_post_calcular_frete_gratis(client):
    """Testa cálculo de frete grátis (acima do limite)."""
    response = client.post('/calcular', 
                           data=json.dumps({'valor_carrinho': 250.00, 'regiao': 'Sudeste'}),
                           content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['frete'] == 0.00

def test_post_calcular_valor_invalido(client):
    """Testa erro com valor inválido de carrinho."""
    response = client.post('/calcular', 
                           data=json.dumps({'valor_carrinho': -10.00, 'regiao': 'Sudeste'}),
                           content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'Valor de carrinho inválido'

def test_post_calcular_regiao_invalida(client):
    """Testa erro com região de entrega inválida."""
    response = client.post('/calcular', 
                           data=json.dumps({'valor_carrinho': 100.00, 'regiao': 'Europa'}),
                           content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'Região de entrega inválida'

def test_post_calcular_sem_corpo(client):
    """Testa erro ao enviar requisição sem corpo."""
    response = client.post('/calcular', 
                           data=json.dumps({}),
                           content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'Valor de carrinho inválido'
