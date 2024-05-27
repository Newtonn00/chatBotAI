import configparser
import os
from src.util.settings_error import SettingsError


class SettingsParser:
    api_key: str

    def __init__(self):

        _settings_file_exists = True
        config = configparser.ConfigParser()
        if os.path.exists(os.environ.get('WORKDIR') + '/settings.ini') is False:
            _settings_file_exists = False
        else:
            config.read(os.environ.get('WORKDIR') + '/settings.ini')
            self.work_dir = os.environ.get('WORKDIR')

        if (os.environ.get('OPENAI_API_KEY') == '' or os.environ.get(
                'OPENAI_API_KEY') is None) and _settings_file_exists and config.has_option('openai', 'openai_api_key'):
            self.openai_api_key = config['openai']['openai_api_key']
        else:
            self.openai_api_key = os.environ.get('OPENAI_API_KEY')

        if (os.environ.get('OPENAI_MODEL') == '' or os.environ.get(
                'OPENAI_MODEL') is None) and _settings_file_exists and config.has_option('openai', 'openai_model'):
            self.openai_model = config['openai']['openai_model']
        else:
            self.openai_model = os.environ.get('OPENAI_MODEL')

        if (os.environ.get('OPENAI_MAX_TOKENS') == '' or os.environ.get(
                'OPENAI_MAX_TOKENS') is None) and _settings_file_exists and config.has_option('openai', 'openai_max_tokens'):
            self.openai_max_tokens = config['openai']['openai_max_tokens']
        else:
            self.openai_max_tokens = os.environ.get('OPENAI_MODEL')

        if (os.environ.get('OPENAI_ASSIST_ID') == '' or os.environ.get(
                'OPENAI_ASSIST_ID') is None) and _settings_file_exists and config.has_option('openai', 'openai_assist_id'):
            self.openai_assist_id = config['openai']['openai_assist_id']
        else:
            self.openai_assist_id = os.environ.get('OPENAI_ASSIST_ID')

        if (os.environ.get('APP_LOG_DIRECTORY') == '' or os.environ.get(
                'APP_LOG_DIRECTORY') is None) and _settings_file_exists and config.has_option('app', 'app_log_directory'):
            self.app_log_directory = config['app']['app_log_directory']
        else:
            self.app_log_directory = os.environ.get('APP_LOG_DIRECTORY')

        if (os.environ.get('APP_DB_DIRECTORY') == '' or os.environ.get(
                'APP_DB_DIRECTORY') is None) and _settings_file_exists and config.has_option('app', 'app_db_directory'):
            self.app_db_directory = config['app']['app_db_directory']
        else:
            self.app_db_directory = os.environ.get('APP_DB_DIRECTORY')

        if (os.environ.get('APP_PORT') == '' or os.environ.get(
                'APP_PORT') is None) and _settings_file_exists and config.has_option('app', 'app_port'):
            self.app_port = config['app']['app_port']
        else:
            self.app_port = os.environ.get('APP_PORT')

        if ((self.openai_api_key == '' or self.openai_api_key is None)
                or (self.openai_model == '' or self.openai_model is None)
                or (self.openai_max_tokens == '' or self.openai_max_tokens is None)
                or (self.openai_assist_id == '' or self.openai_assist_id is None)
                or (self.app_db_directory == '' or self.app_db_directory is None)
                or (self.app_log_directory == '' or self.app_log_directory is None)
                or (self.app_port == '' or self.app_port is None)
            ):
            raise SettingsError()
