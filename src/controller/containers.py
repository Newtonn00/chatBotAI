from dependency_injector import providers, containers

from src.util.settings_parser import SettingsParser
from src.controller.openai_engine import OpenAIClient
from src.business.chatbot_service import ChatBotService
from src.controller.sqlite_engine import SQLiteEngine
from src.repository.user_repository import UserRepository
from src.repository.message_repository import ThreadRepository


class Containers(containers.DeclarativeContainer):
    settings_parser = providers.Singleton(SettingsParser)

    openai_client = providers.Singleton(OpenAIClient, settings_parser)
    sqlite_engine = providers.Singleton(SQLiteEngine)
    user_repo = providers.Factory(UserRepository, sqlite_engine)
    thread_repo = providers.Factory(ThreadRepository, sqlite_engine)
    chatbot_service = providers.Factory(ChatBotService, openai_client, user_repo, thread_repo)


