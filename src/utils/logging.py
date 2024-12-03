import logging
from colorama import Fore, Style

CONSOLE_LOG_FORMAT = '%(asctime)s %(levelname)s %(name)s %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class ColoredFormatter(logging.Formatter):
    """Logging formatter that adds colors to the log messages."""

    LEVEL_COLORS = {
        'DEBUG': Fore.GREEN,
        'INFO': Fore.BLUE,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA,
    }

    def format(self, record):
        """Format the log message."""

        levelname = record.levelname
        colored_levelname = f'{self.LEVEL_COLORS.get(levelname, Fore.WHITE)}{Style.BRIGHT}{levelname}{Style.RESET_ALL}'

        levelname_length = len(levelname)
        spacing = ' ' * (8 - levelname_length)

        name = record.name
        colored_name = f'{Fore.MAGENTA}{name}{Style.RESET_ALL}'

        formatted_message = self._fmt % {
            'levelname': colored_levelname + spacing,
            'name': colored_name,
            'message': record.getMessage(),
            'asctime': self.formatTime(record, self.datefmt),
        }
        formatted_message = formatted_message.replace(
            '{levelname}', colored_levelname + spacing
        )
        formatted_message = formatted_message.replace('{name}', colored_name)

        return formatted_message


def get_logger(name: str) -> logging.Logger:
    """Get a logger with the specified name."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        ColoredFormatter(CONSOLE_LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
    )
    logger.addHandler(console_handler)

    return logger
