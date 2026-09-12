import pytest
from frete import calcular_frete

def test_calcular_frete_norte_abaixo_limite():
    # Norte: limite R$ 300.00. Carrinho R$ 150.00. Deve cobrar frete.
    # Frete padrão Norte: R$ 50.00
    assert calcular_frete(150.00, "Norte") == 50.00

def test_calcular_frete_norte_exato_no_limite():
    # Norte: limite R$ 300.00. Carrinho R$ 300.00. Deve zerar o frete.
    assert calcular_frete(300.00, "Norte") == 0.00

def test_calcular_frete_norte_acima_limite():
    # Norte: limite R$ 300.00. Carrinho R$ 300.01. Deve zerar o frete.
    assert calcular_frete(300.01, "Norte") == 0.00

def test_calcular_frete_outras_regioes_abaixo_limite():
    # Sudeste: limite R$ 200.00. Carrinho R$ 150.00. Deve cobrar frete.
    # Frete padrão Sudeste: R$ 15.00
    assert calcular_frete(150.00, "Sudeste") == 15.00

def test_calcular_frete_outras_regioes_no_limite():
    # Sudeste: limite R$ 200.00. Carrinho R$ 200.00. Deve zerar o frete.
    assert calcular_frete(200.00, "Sudeste") == 0.00

def test_calcular_frete_outras_regioes_acima_limite():
    # Sudeste: limite R$ 200.00. Carrinho R$ 250.00. Deve zerar o frete.
    assert calcular_frete(250.00, "Sudeste") == 0.00

def test_calcular_frete_valor_invalido_zero():
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_frete(0, "Norte")

def test_calcular_frete_valor_invalido_negativo():
    with pytest.raises(ValueError, match="Valor de carrinho inválido"):
        calcular_frete(-10.00, "Norte")

def test_calcular_frete_regiao_invalida():
    with pytest.raises(ValueError, match="Região de entrega inválida"):
        calcular_frete(100.00, "Europa")

def test_calcular_frete_regiao_vazia():
    with pytest.raises(ValueError, match="Região de entrega inválida"):
        calcular_frete(100.00, "")

def test_calcular_frete_case_insensitive_and_whitespace():
    # Região com espaços e letras minúsculas/maiúsculas misturadas
    assert calcular_frete(350.00, "  norte  ") == 0.00
    assert calcular_frete(250.00, "  SUDESTE  ") == 0.00
