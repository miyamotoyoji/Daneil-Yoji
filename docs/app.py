import os
import sys
from flask import Flask, render_template, request, jsonify

# Adicionar o diretório atual ao path para garantir que a importação do frete funcione
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from frete import calcular_frete

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    """Serves the main page."""
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    """
    Calculates freight based on request data.
    Supports JSON body.
    """
    data = request.get_json() or {}
    
    # Suporta tanto "valor" quanto "valor_carrinho"
    valor_carrinho = data.get('valor_carrinho')
    if valor_carrinho is None:
        valor_carrinho = data.get('valor')
        
    regiao = data.get('regiao')
    
    # Validações prévias de existência de campos
    if valor_carrinho is None:
        return jsonify({'error': 'Valor de carrinho inválido'}), 400
        
    if regiao is None:
        return jsonify({'error': 'Região de entrega inválida'}), 400

    try:
        # Conversão para float e validação
        try:
            valor_carrinho_float = float(valor_carrinho)
        except (ValueError, TypeError):
            return jsonify({'error': 'Valor de carrinho inválido'}), 400
            
        # Executa a regra de negócio
        valor_frete = calcular_frete(valor_carrinho_float, regiao)
        return jsonify({
            'success': True,
            'frete': valor_frete,
            'valor_carrinho': valor_carrinho_float,
            'regiao': regiao
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Ocorreu um erro interno ao processar o cálculo.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
