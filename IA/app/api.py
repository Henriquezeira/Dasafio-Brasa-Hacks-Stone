from flask import Flask, request, jsonify
from app.data_processing import load_data
from app.models.model import train_modelgit

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    try:
        predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df = load_data()
        model = train_model(predial_df, impostos_df, produtos_df, funcionarios_df, prolabore_df)
        
        # Aqui você pode adicionar a lógica para salvar o modelo ou fornecer uma resposta ao usuário
        return jsonify({'message': 'Modelo treinado com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
