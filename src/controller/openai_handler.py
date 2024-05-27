import time
import logging

from openai import OpenAI, OpenAIError


class OpenAIHandler():
    def __init__(self, openai_client):
        self._model = openai_client.get_model()
        self._assistant_id = openai_client.get_assist_id()
        self._openai_client: OpenAI = openai_client.get_instance()
        self._max_tokens = openai_client.get_max_tokens()
        self._logger = logging.getLogger("")

    def get_new_user_thread_id(self):
        thread_id = -1
        try:
            thread = self._openai_client.beta.threads.create()
            thread_id = thread.id
        except OpenAIError as err:
            self._logger.error(f'Error during Open AI Thread creating: {err}')
        return thread_id

    def generate_request(self, user_thread_id, user_content):
        bot_answer = ""
        try:
            self._openai_client.beta.threads.messages.create(
                thread_id=user_thread_id,
                role="user",
                content=user_content

            )

            self._logger.info(f'Message added to thread {user_thread_id}')

            run = self._openai_client.beta.threads.runs.create(
                thread_id=user_thread_id,
                assistant_id=self._assistant_id
            )

            self._logger.info(f'Ran users thread {user_thread_id}, run - {run.id} ')

            while run.status != "completed":
                run = self._openai_client.beta.threads.runs.retrieve(
                    thread_id=user_thread_id,
                    run_id=run.id
                )
                time.sleep(1)
            response = self._openai_client.beta.threads.messages.list(thread_id=user_thread_id)
            bot_answer = response.data[0].content[0].text.value
            self._logger.info(f'Bots answer for users thread {user_thread_id} received')
        except OpenAIError as err:
            self._logger.error(f'Error during receiving bots answer in users thread {user_thread_id}: {err}')

        return bot_answer
