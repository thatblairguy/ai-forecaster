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
    try:
        with open(config_file, encoding=encoding) as f:
            d = json.load(f)
            return Configuration(d)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {config_file}: {e}")
        return None
    except FileNotFoundError as e:
        print(f"Configuration file not found: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
