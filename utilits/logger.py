from loguru import logger


class LogConfig:

    @staticmethod
    def set_logger_config():
        logger.remove()
        return logger.add(
            "logging_data.log",
            format="{time:YYYY-MM-DD at HH:mm:ss} {name} {level} {message}",
            level="INFO",
            rotation="1 MB",
            compression="zip"
        )
