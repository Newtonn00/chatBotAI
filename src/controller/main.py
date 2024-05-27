from src.controller.containers import Containers
from src.controller.app_manager import AppManager
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

container = Containers()

log_directory = container.settings_parser().work_dir + container.settings_parser().app_log_directory + "/app.log"

timed_handler = TimedRotatingFileHandler(log_directory,
                                         when='midnight', interval=1, backupCount=10)
timed_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        timed_handler,
                        logging.StreamHandler(sys.stdout)
                            ]
                    )

app_manager = container.app_manager()
AppManager.set_container_instance(container)
app_manager.run()

