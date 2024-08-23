from flask import Flask, request, jsonify
from data_processing import load_data, preprocess_data
from model import train_model

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    # Carregar e pré-processar os dados
    bank_df, sales_df, _ = load_data()
    bank_df, sales_df = preprocess_data(bank_df, sales_df)
    
    # Treinar o modelo
    model = train_model(bank_df)
    
    # Aqui você pode salvar o modelo treinado se desejar
    # joblib.dump(model, 'model.pkl')
    
    return jsonify({"message": "Model trained successfully"})

if __name__ == '__main__':
    app.run(debug=True)
