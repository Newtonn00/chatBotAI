from flask import Flask, request, jsonify, app


class AppManager:
    container = None

    @classmethod
    def set_container_instance(cls, container_instance):
        cls.container = container_instance

    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/chat', methods=['POST'])
        def chat():
            user_input = request.json['message']
            username = request.json['username']
            bot_response = self.container.chatbot_service().handle_user_message(username, user_input)
            return jsonify({'response': bot_response})

    def run(self, port=3055):
        self.app.run(port=port, host="0.0.0.0", debug=False)
