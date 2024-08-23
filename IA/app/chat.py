from flask import Blueprint, request, jsonify

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/message', methods=['POST'])
def handle_message():
    user_message = request.json.get('message')
    # Aqui você chamará a função da IA para gerar uma resposta
    response = generate_response(user_message)
    return jsonify({'response': response})

def generate_response(message):
    # Função de exemplo, substitua com a lógica da IA
    return f"Você disse: {message}"
