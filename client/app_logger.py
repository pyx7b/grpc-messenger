import logging

def setup_logger(log_file="app.log"):
    # Create a logger
    logger = logging.getLogger("APP")
    logger.setLevel(logging.DEBUG)

    # Create a file handler to log to a file
    #file_handler = logging.FileHandler(log_file)
    #file_handler.setLevel(logging.DEBUG)

    # Create a console handler to log to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter to format log messages
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Set the formatter for the file and console handlers
    #file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    #logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger