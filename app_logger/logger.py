import logging
import os

from datetime import datetime
from colorlog import ColoredFormatter


class Logger:
    LOG_FORMAT = 'PID %(process)d - %(threadName)s - %(asctime)s - %(log_color)s%(name)s - %(log_color)s%(levelname)s - %(message)s'
    # formatter = logging.Formatter(
    #     LOG_FORMAT
    # )
    formatter = ColoredFormatter(LOG_FORMAT)
    log_file_path = os.path.join(
        os.path.dirname(__file__), f'{datetime.now().date().isoformat()}-logs.log'
    )

    # create console handler, set level to debug, and set formatter
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    # create file handler, set level, and set formatter
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    def __init__(self, section_name: str = 'APP'):
        # create logger
        self.logger = logging.getLogger(section_name)
        self.logger.setLevel(logging.DEBUG)

        # add ch to logger
        self.logger.addHandler(self.ch)
        self.logger.addHandler(self.fh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg, exc_info=True)


wrapper_logger = Logger()


def function_io_decorator(func):
    def wrapper(*args, **kwargs):
        wrapper_logger.info(f'Entering function --> {func.__name__}')
        result = func(*args, **kwargs)
        wrapper_logger.info(f'Exiting function --> {func.__name__} \n RESULT--> {result}')
        return result

    return wrapper
