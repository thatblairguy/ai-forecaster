import json

"""
Configuration objects for the forecast program.
"""

class AISource:

    def __init__(self, host: str, model: str) -> None:
        self.host = host
        self.model = model


class Configuration:

    def __init__(self, raw_config: dict) -> None:
        self.email = raw_config["email"]
        self.location = (raw_config["location"]["latitude"], raw_config["location"]["longitude"])
        self.ai = AISource(raw_config["ai"]["server"], raw_config["ai"]["model"])


def load(config_file: str):
    with open(config_file) as f:
        d = json.load(f)
        return Configuration(d)
