import logging

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Create a logger object
logger = logging.getLogger(__name__)

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)

def log_debug(message):
    logger.debug(message)