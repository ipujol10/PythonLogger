from .CustomLogger import CustomLogging, logging


def set_logger(
    *,
    level: int = logging.INFO,
    format: str = "[%(levelname)s] %(asctime)s - %(message)s (%(filename)s:%(lineno)d)"
) -> None:
    logging.basicConfig(level=level, format=format)

def get_logger(
    name: str = "",
    *,
    level: int = logging.INFO,
    format: str = "[%(levelname)s] %(asctime)s - %(message)s (%(filename)s:%(lineno)d)"
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(CustomLogging(format=format))

    logger.addHandler(ch)
    return logger
