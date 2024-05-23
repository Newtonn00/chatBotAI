

class OpenAIHandler():
    def __init__(self, openai_client, model):
        self._model = model
        self._openai_client = openai_client.get_instance()

    def generate_thread_id(self):
        return None

    def make_request(self, messages, thread_id):
        response = self._openai_client.ChatCompletion.create(
            model=self._model,
            messages=messages,
            max_tokens=150,
            temperature=0.7,
            thread_id=thread_id
        )
        return response.choices[0].message['content'].strip()
