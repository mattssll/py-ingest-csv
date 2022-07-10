import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
            logging.FileHandler("./logger/logs.log", mode='w'),
            logging.StreamHandler()
        ]
    )


logger = logging.getLogger()
logger.info("Debug logging test...")
