import logging

class CustomLogging(logging.Formatter):
    green = "\x1b[92;1m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, *, format: str):
        logging.Formatter.__init__(self, format)
        self.FORMATS = {
            logging.DEBUG: self.green + format + self.reset,
            logging.INFO: self.grey + format + self.reset,
            logging.WARNING: self.yellow + format + self.reset,
            logging.ERROR: self.red + format + self.reset,
            logging.CRITICAL: self.bold_red + format + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)