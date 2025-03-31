from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Caminho absoluto para o arquivo CSV
CSV_PATH = 'C:/Users/Admin/Documents/processo_seletivo_estagio/teste_api/data/Relatorio_cadop_operadoras.csv'

# Tente carregar o CSV
try:
    df_operadoras = pd.read_csv(CSV_PATH, delimiter=';')
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV: {e}")
    df_operadoras = None

@app.route('/operadoras', methods=['GET'])
def buscar_operadoras():
    if df_operadoras is None:
        return jsonify({"error": "Falha ao carregar os dados das operadoras"}), 500

    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])

    # Filtra os dados baseados na consulta
    resultados = df_operadoras[df_operadoras.apply(lambda row: query in row.to_string().lower(), axis=1)]
    
    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)