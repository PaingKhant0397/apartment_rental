
import logging


def setup_logger(name):
    """Set up and return a logger with a given name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter for normal logging
    normal_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create formatter for error logging
    error_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

    # Set the normal formatter for the console handler
    console_handler.setFormatter(error_formatter)
    logger.addHandler(console_handler)

    logger.normal_formatter = normal_formatter
    logger.error_formatter = error_formatter

    return logger
