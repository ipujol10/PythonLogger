import logging


def set_logger(
    *,
    level: int = logging.INFO,
    format: str = "[%(levelname)s] %(asctime)s - %(message)s (%(filename)s:%(lineno)d)"
) -> None:
    logging.basicConfig(level=level, format=format)
