
# Especificação: Sistema de cálculo de Frete

## Requisitos Funcionais
- **RF-01 (Event-Driven):** WHEN o usuário calcular o frete e o carrinho atingir o limite regional, THE SYSTEM SHALL zerar o frete.
- **RF-02 (Event-Driven):** WHEN o usuário informar uma região de entrega válida, THE SYSTEM SHALL identificar a região e aplicar o limite de frete correspondente.
- **RF-03 (Event-Driven):** WHEN o usuário alterar a região de entrega, THE SYSTEM SHALL recalcular automaticamente o valor do frete de acordo com a nova região.

## Regras de Negócio e Exceções
- **RB-01 (State-Driven):** WHILE a região for "Norte", THE SYSTEM SHALL considerar R$ 300,00 como valor limite para frete grátis. Para as demais regiões, o limite é R$ 200,00.
- **RB-02 (Unwanted Behavior):** IF valor <= 0, THEN exibir erro cast, 'Valor de carrinho inválido'.
- **RB-03 (Unwanted Behavior):** IF a região informada não estiver cadastrada THEN exibir erro "Região de entrega inválida".