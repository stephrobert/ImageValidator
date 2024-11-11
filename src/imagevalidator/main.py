# src/main.py
import sys
import os
import click
from imagevalidator.config import Config
from imagevalidator.log_config import setup_logging


@click.command()
@click.option('--config', '-c', default='config.yaml', help='Path to the config file')
def main(config):
    config = Config(config)
    setup_logging(config.get('logging'))

if __name__ == '__main__':
    main()
