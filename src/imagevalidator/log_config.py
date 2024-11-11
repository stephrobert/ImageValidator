# src/log_config.py
import logging

def setup_logging(logging_config):
    log_format = logging_config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_level = logging_config.get('level', 'INFO').upper()

    logging.basicConfig(
        format=log_format,
        level=getattr(logging, log_level, logging.INFO),
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.info("Logging configuré avec succès")
