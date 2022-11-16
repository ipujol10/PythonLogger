import logging
from enum import Enum


class Levels(Enum):
    Debug = logging.DEBUG
    Info = logging.INFO
    Error = logging.ERROR


def set_logger(
    *,
    level: Levels = Levels.Info.value,
    format: str = "[%(levelname)s] %(asctime)s - %(message)s"
) -> None:
    logging.basicConfig(level=level, format=format)
