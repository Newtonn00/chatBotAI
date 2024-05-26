from src.controller.containers import Containers
from src.controller.app_manager import AppManager


container = Containers()
app_manager = container.app_manager()
AppManager.set_container_instance(container)
app_manager.run()

