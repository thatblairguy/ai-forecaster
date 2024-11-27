import json
from lib.location import *
from lib.persona import *
from lib.aisource import *

"""
Configuration objects for the forecast program.
"""


class Configuration:

    def __init__(self, raw_config: dict) -> None:
        self.email = raw_config["email"]
        self.ai = AISource(raw_config["ai"]["server"], raw_config["ai"]["model"])
        self.locations = [
            Location(loc["city"], (loc["latitude"], loc["longitude"]))
            for loc in raw_config["locations"]
        ]
        self.output_location = raw_config["output-location"]
        self.personalities = [
            Persona(p["persona"], p["style"]) for p in raw_config["personalities"]
        ]


def load(config_file: str, encoding='utf-8'):
    with open(config_file) as f:
        d = json.load(f)
        return Configuration(d)
