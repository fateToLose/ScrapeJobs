import logging
import logging.handlers

from datetime import datetime

from ..config.settings import LogConfig

def setup_logging(config: LogConfig, logger_name: str | None = None) -> logging.Logger:
    """Setup logging with rotation and proper formatting."""
    
    logger: logging.Logger = logging.getLogger(logger_name or __name__)
    today: str = datetime.now().strftime("%Y-%m-%d")
    
    # Clear existing handlers to avoid duplicates
    logger.handlers.clear()
    logger.setLevel(config.level.value)
    
    # Create formatter
    formatter = logging.Formatter(config.format)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if config.file_path:
        file_handler = logging.handlers.RotatingFileHandler(
            config.file_path / f"{today}.log",
            maxBytes=config.max_file_size,
            backupCount=config.backup_count
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    # Prevent propagation to root logger if not desired
    logger.propagate = False
    
    logger.info("Application logging initialized")
    logger.debug(f"Log level: {config.level.value}")
    logger.debug(f"Log file: {config.file_path or 'Console only'}")
    
    return logger