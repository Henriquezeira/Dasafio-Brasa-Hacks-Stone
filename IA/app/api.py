from flask import Flask, request, jsonify
from app.data_processing import load_data
from app.models.model import train_model

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    try:
        # Carregando os dados do Excel
        predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df = load_data()
        
        # Treinando o modelo com os dados carregados
        model = train_model(predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df)
        
        # Retornando uma resposta ao usuário
        return jsonify({'message': 'Modelo treinado com sucesso!'})
    except Exception as e:
        # Em caso de erro, retornar a mensagem de erro com o status 500
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
