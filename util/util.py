import datetime
import logging
import logging.handlers
import os


def get_logger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    path = os.path.dirname(os.path.dirname(__file__)) + '\\logs'

    rf_handler = logging.handlers.TimedRotatingFileHandler(path + '\\' + 'all.log', when='midnight', interval=1,
                                                           backupCount=7, encoding='utf-8',
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    f_handler = logging.FileHandler(path + '\\' + 'error.log', encoding='utf-8')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger
