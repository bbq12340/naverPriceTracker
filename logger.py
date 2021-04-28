import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logs/ERROR.log')

# Create formatters and add it to handlers
c_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
f_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

f_handler.setLevel(logging.ERROR)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
