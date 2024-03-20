import logging
from config import LOG_PATH, DEBUG_MODE
from datetime import datetime


class Logger:
    def __init__(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        log_name = f"{LOG_PATH}/{current_datetime}.log"
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filename=log_name,
            filemode="a",
        )
        self.logger = logging.getLogger()

    def info(self, msg, only_debug_mode=False):
        if only_debug_mode == True and DEBUG_MODE != True:
            return
        self.logger.info(msg)

    def warning(self, msg, only_debug_mode=False):
        if only_debug_mode == True and DEBUG_MODE != True:
            return
        self.logger.warning(msg)

    def error(self, msg, only_debug_mode=False):
        if only_debug_mode == True and DEBUG_MODE != True:
            return
        self.logger.error(msg)


logger = Logger()
