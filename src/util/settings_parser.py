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

        if self.openai_api_key == '' or self.openai_api_key is None:
            raise SettingsError()
