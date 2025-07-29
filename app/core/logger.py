import logging


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] [%(filename)s - LINE:%(lineno)d] %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")