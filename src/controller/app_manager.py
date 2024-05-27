import logging

from flask import Flask, request, jsonify, abort


class AppManager:
    container = None

    @classmethod
    def set_container_instance(cls, container_instance):
        cls.container = container_instance

    def __init__(self):
        self.app = Flask(__name__)
        self._logger = logging.getLogger("")

        @self.app.route('/chat', methods=['POST'])
        def chat():
            try:
                user_input = request.json['message']
                username = request.json['username']
                if not user_input or not username:
                    raise Exception("Invalid request: 'thread_id' and 'content' are required")
            except Exception as err:
                self._logger.error(f'Requests attributes error: {err}')
                abort(400, description="Invalid request: 'thread_id' and 'content' are required")

            self._logger.info(f'Users request received ({username})')

            bot_response = self.container.chatbot_service().handle_user_message(username, user_input)

            if bot_response:
                self._logger.info(f'Bot response is sending ({request.json["username"]})')
            else:
                abort(500, description="Inner error occurred")
            return jsonify({'response': bot_response["response"]})

        @self.app.errorhandler(500)
        def inner_error(error):
            return jsonify({'error': str(error)}), 500

        @self.app.errorhandler(400)
        def bad_request(error):
            return jsonify({'error': str(error)}), 400

    def run(self, port=3055):
        self.app.run(port=self.container.settings_parser().app_port, host="0.0.0.0", debug=False)
