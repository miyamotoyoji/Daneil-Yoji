from typing import cast

REGIOES_VALIDAS = {
    "Norte": {"limite": 300.00, "valor": 50.00},
    "Nordeste": {"limite": 200.00, "valor": 40.00},
    "Centro-Oeste": {"limite": 200.00, "valor": 30.00},
    "Sudeste": {"limite": 200.00, "valor": 15.00},
    "Sul": {"limite": 200.00, "valor": 20.00}
}

def calcular_frete(valor_carrinho: float, regiao: str) -> float:
    """
    Calcula o frete com base no valor do carrinho e na região do destinatário.
    Aplica limites regionais para frete grátis.
    """
    # Validação do valor do carrinho (RB-02)
    try:
        valor_float = float(valor_carrinho)
    except (ValueError, TypeError):
        raise ValueError('Valor de carrinho inválido')
        
    if valor_float <= 0:
        raise ValueError('Valor de carrinho inválido')
        
    # Garantindo o tipo com typing.cast se necessário para estática
    valor_float = cast(float, valor_float)
        
    # Validação da região (RB-03)
    if not isinstance(regiao, str):
        raise ValueError('Região de entrega inválida')
        
    regiao_normalizada = regiao.strip().title()
    
    if regiao_normalizada not in REGIOES_VALIDAS:
        raise ValueError('Região de entrega inválida')
        
    info_regiao = REGIOES_VALIDAS[regiao_normalizada]
    limite = info_regiao["limite"]
    valor_frete_padrao = info_regiao["valor"]
    
    # Se atingir o limite regional, zera o frete (RF-01)
    if valor_float >= limite:
        return 0.0
        
    return valor_frete_padrao
