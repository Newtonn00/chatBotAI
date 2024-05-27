from dependency_injector import providers, containers

from src.util.settings_parser import SettingsParser
from src.controller.openai_engine import OpenAIClient
from src.business.chatbot_service import ChatBotService
from src.controller.sqlite_engine import SQLiteEngine
from src.repository.user_repository import UserRepository
from src.repository.thread_repository import ThreadRepository
from src.repository.message_repository import MessageRepository
from src.controller.app_manager import AppManager
from src.controller.openai_handler import OpenAIHandler


class Containers(containers.DeclarativeContainer):
    settings_parser = providers.Singleton(SettingsParser)

    openai_client = providers.Singleton(OpenAIClient, settings_parser)
    sqlite_engine = providers.Singleton(SQLiteEngine, settings_parser)
    user_repo = providers.Factory(UserRepository, sqlite_engine)
    thread_repo = providers.Factory(ThreadRepository, sqlite_engine)
    message_repo = providers.Factory(MessageRepository, sqlite_engine)
    openai_handler = providers.Factory(OpenAIHandler, openai_client)
    chatbot_service = providers.Factory(ChatBotService, openai_handler, user_repo, thread_repo, message_repo)
    app_manager = providers.Factory(AppManager)

