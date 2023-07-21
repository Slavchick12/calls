"""Project logger module."""

import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

LOGS_PATH = 'calls/logging/logs'
BACKUP_COUNT = 30

os.makedirs(LOGS_PATH, exist_ok=True)


class Logger(object):
    """Default logger for project."""

    logger = logging.getLogger('calls_logger')
    handler_log_rotation = TimedRotatingFileHandler(
        f'{LOGS_PATH}/calls_loggs.log',
        when='D',
        interval=1,
        backupCount=BACKUP_COUNT,
        encoding='utf-8',
    )
    handler_stdout = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')


calls_logger = Logger()
logger = calls_logger.logger
logger.setLevel(logging.INFO)
calls_logger.handler_stdout.setFormatter(calls_logger.formatter)
calls_logger.handler_stdout.setFormatter(calls_logger.formatter)
logger.addHandler(calls_logger.handler_log_rotation)
logger.addHandler(calls_logger.handler_stdout)
