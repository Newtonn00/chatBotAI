from openai import OpenAI


class OpenAIClient:

    def __init__(self, config):
        self._openai_client = OpenAI(api_key=config.openai_api_key)
        self._model = config.openai_model
        self._max_tokens = config.openai_max_tokens

    def get_instance(self):
        return self._openai_client

    def get_model(self):
        return self._model

    def get_max_tokens(self):
        return self._max_tokens

