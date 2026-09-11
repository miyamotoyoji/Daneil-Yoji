RF-01: WHEN o usuario calcular o frete e o carrinho atingir o limite regional, THE SYSTEM SHALL zerar o frete
RB-01: WHILE a região for"Norte", o limite é R$ 300,00. Demais regiões: R$ 200,00.
RB-02: IF valor <= 0, THEN exibir erro cast, 'Valor de carrinho inválido'
RF-02: WHEN o usuário informar uma região de entrega válida, THE SYSTEM SHALL identificar a região e aplicar o limite de frete correspondente.
RB-03: IF a região informada não estiver cadastrada THEN exibir erro "Região de entrega inválida".
RF-03: WHEN o usuário alterar a região de entrega, THE SYSTEM SHALL recalcular automaticamente o valor do frete de acordo com a nova região.
