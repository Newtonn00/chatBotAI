from src.entity.user_entity import UserEntity
from src.entity.message_entity import MessageEntity


class ChatBotService:

    def __init__(self, ai_client, user_repo, thread_repo):
        self._ai_client = ai_client
        self._user_repo = user_repo
        self._thread_repo = thread_repo

    def _get_user(self, username) -> UserEntity:
        return self._user_repo.read(username)

    def _create_new_user(self, username) -> UserEntity:
        return self._user_repo.create(username)

    def get_or_create_thread(self, user):
        thread = session.query(Thread).filter_by(user_id=user.id).first()
        if not thread:
            thread_id = self._ai_client.generate_thread_id()
            thread = Thread(user_id=user.id, thread_id=thread_id)
            session.add(thread)
            session.commit()
        return thread

    def get_thread_messages(self, thread):
        messages = session.query(Message).filter_by(thread_id=thread.id).all()
        return [
            {"role": "user", "content": msg.content} if i % 2 == 0 else {"role": "assistant", "content": msg.content}
            for i, msg in enumerate(messages)]

    def _get_user_messages(self, user_id) -> list:
        messages_dataclass = self._thread_repo.read(user_id)
        messages_history = [{"role": message.role,
                             "content": message.message_text} for message in messages_dataclass]

        return messages_history

    def summarize_conversation(self, conversation):
        response = self._ai_client.make_request(f"Суммаризируй следующую беседу:\n\n{conversation}\n\n", thread_id=0)
        return response.choices[0].text.strip()

    def handle_user_message(self, username, user_message):
        user_id = self._get_user(username).id
        if not user_id:
            user_id = self._create_new_user(username)

        user_message_history = self._get_user_content(user_id)

        thread = self.get_or_create_thread(user_id)
        bot_response = self._ai_client.generate_request(thread_messages, thread.thread_id)

        # Сохранение сообщений в базу данных
        user_msg = Message(thread_id=thread.id, content=user_message)
        bot_msg = Message(thread_id=thread.id, content=bot_response)
        session.add_all([user_msg, bot_msg])
        session.commit()

        # Обобщение беседы после окончания для сохранения контекста
        conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in thread_messages])
        summary = self.summarize_conversation(conversation)
        thread.summary = summary
        session.commit()

        return bot_response
