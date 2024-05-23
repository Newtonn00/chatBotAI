from dependency_injector import providers, containers

from src.util.settings_parser import SettingsParser
from src.controller.openai_engine import OpenAIClient


class Containers(containers.DeclarativeContainer):
    settings_parser = providers.Singleton(SettingsParser)

    openai_client = providers.Singleton(OpenAIClient, settings_parser)
