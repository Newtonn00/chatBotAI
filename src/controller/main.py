from flask import Flask, request, jsonify
import src.business.chatbot_service as chatbot

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    username = request.json['username']
    bot_response = chatbot.handle_user_message(username, user_input)
    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(port=5060, debug=True)
