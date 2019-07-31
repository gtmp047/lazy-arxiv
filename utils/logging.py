from logging import getLevelName, getLogger, LoggerAdapter, FileHandler, Formatter

from utils.interactions import CONFIG, LOG_FILE_PATH, PROJECT_NAME


def setup_logging():
    log_level = getLevelName(CONFIG.logging.get('level') or 'ERROR')
    log_formatter = Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    log_handler = FileHandler(filename=LOG_FILE_PATH,
                              mode='a',
                              encoding='utf-8')
    log_handler.setFormatter(log_formatter)

    logger = getLogger(PROJECT_NAME)

    logger.setLevel(log_level)
    logger.addHandler(log_handler)


def set_handler_logger(name: str):
    logger = getLogger(PROJECT_NAME)
    logger.name = name
    return logger