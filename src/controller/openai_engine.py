from openai import OpenAI


class OpenAIClient:

    def __init__(self, config):
        self._openai_client = OpenAI(api_key=config.openai_api_key)

    def get_instance(self):
        return self._openai_client


