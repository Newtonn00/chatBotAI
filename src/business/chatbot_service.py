from src.entity.user_entity import UserEntity
from src.entity.thread_entity import ThreadEntity
import logging


class ChatBotService:

    def __init__(self, ai_handler, user_repo, thread_repo, message_repo):
        self._ai_handler = ai_handler
        self._user_repo = user_repo
        self._thread_repo = thread_repo
        self._message_repo = message_repo
        self._logger = logging.getLogger("")

    def _get_user(self, username) -> UserEntity:
        return self._user_repo.read(username)

    def _create_new_user(self, username) -> UserEntity:
        return self._user_repo.create(username)

    def _get_user_thread(self, user_id) -> ThreadEntity:

        return self._thread_repo.read(user_id)

    def _create_user_thread(self, user_id) -> ThreadEntity:
        thread_id = self._ai_handler.get_new_user_thread_id()
        thread_dataclass = self._thread_repo.create(user_id=user_id, thread_id=thread_id, active=True)
        return thread_dataclass

    def _get_user_messages(self, user_id) -> list:
        messages_dataclass = self._thread_repo.read(user_id)
        messages_history = [{"role": message.role,
                             "content": message.message_text} for message in messages_dataclass]

        return messages_history

    def handle_user_message(self, username, user_message):
        user_data: UserEntity = self._get_user(username)
        if user_data:
            user_id = user_data.id
        else:
            user_id = self._create_new_user(username).id

        if not user_id:
            return {"OK": False, "response": ""}

        thread_data: ThreadEntity = self._get_user_thread(user_id)
        if thread_data:
            thread_id = thread_data.thread_id
        else:
            thread_id = self._create_user_thread(user_id).thread_id

        if not thread_id:
            return {"OK": False, "response": ""}

        bot_response = self._ai_handler.generate_request(thread_id, user_message)

        if not bot_response:
            return {"OK": False, "response": ""}

        self._message_repo.create(thread_id=thread_id, message_text=user_message, role="user", user_id=user_id)
        self._message_repo.create(thread_id=thread_id, message_text=bot_response, role="bot", user_id=user_id)

        return {"OK": True, "response": bot_response}
