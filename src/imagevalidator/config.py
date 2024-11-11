# src/config.py
import yaml

class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as stream:
            self.config = yaml.safe_load(stream)

    def get(self, key, default=None):
        return self.config.get(key, default)
