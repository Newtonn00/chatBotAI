import time

from openai import OpenAI


class OpenAIHandler():
    def __init__(self, openai_client):
        self._model = openai_client.get_model()
        self._assistant_id = openai_client.get_assist_id()
        self._openai_client: OpenAI = openai_client.get_instance()
        self._max_tokens = openai_client.get_max_tokens()

    def get_new_user_thread_id(self):
        thread = self._openai_client.beta.threads.create()
        return thread.id

    def generate_request(self, user_thread_id, user_content):

        self._openai_client.beta.threads.messages.create(
            thread_id=user_thread_id,
            role="user",
            content=user_content

        )
        run = self._openai_client.beta.threads.runs.create(
            thread_id=user_thread_id,
            assistant_id=self._assistant_id
        )

        while run.status != "completed":
            run = self._openai_client.beta.threads.runs.retrieve(
                thread_id=user_thread_id,
                run_id=run.id
            )
            time.sleep(1)
        response = self._openai_client.beta.threads.messages.list(thread_id=user_thread_id)
        return response.data[0].content[0].text.value
