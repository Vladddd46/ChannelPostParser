import logging
from config import LOG_PATH, DEBUG_MODE, LOG_ENABLED, WRITE_LOG_IN_STDOUT
from datetime import datetime


class Logger:
    def __init__(self):
        if LOG_ENABLED:
            self.logger = logging.getLogger()
            self.logger.handlers = []
            self.logger.setLevel(logging.INFO)
            if WRITE_LOG_IN_STDOUT:
                # Add a StreamHandler to write logs to stdout
                stream_handler = logging.StreamHandler()
                stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
                self.logger.addHandler(stream_handler)
            else:
                current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
                log_name = f"{LOG_PATH}/{current_datetime}.log"
                file_handler = logging.FileHandler(log_name, mode='a')
                file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
                self.logger.addHandler(file_handler)

    def info(self, msg, only_debug_mode=False):
        if only_debug_mode == True and DEBUG_MODE != True:
            return
        if LOG_ENABLED == True:
            self.logger.info(msg)

    def warning(self, msg, only_debug_mode=False):
        if only_debug_mode == True and DEBUG_MODE != True:
            return
        if LOG_ENABLED == True:
            self.logger.warning(msg)

    def error(self, msg, only_debug_mode=False):
        if only_debug_mode == True and DEBUG_MODE != True:
            return
        if LOG_ENABLED == True:
            self.logger.error(msg)


logger = Logger()
