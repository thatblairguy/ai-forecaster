import json

"""
Configuration objects for the forecast program.
"""

class Configuration:

    def __init__(self, raw_config: dict) -> None:
        self.email = raw_config["email"]
        self.location = (raw_config["location"]["latitude"], raw_config["location"]["longitude"])
        self.ai = AISource(raw_config["ai"]["server"], raw_config["ai"]["model"])
        self.personalities = [Persona(p["persona"], p["style"]) for p in raw_config["personalities"]]


class AISource:

    def __init__(self, host: str, model: str) -> None:
        self.host = host
        self.model = model


class Persona:

    def __init__(self, persona: str, style: str) -> None:
        self.persona = persona
        self.style = style


def load(config_file: str):
    with open(config_file) as f:
        d = json.load(f)
        return Configuration(d)
