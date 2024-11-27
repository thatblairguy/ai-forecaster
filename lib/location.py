import re
from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longitude: float


class Location:
    """
    Represents a location and provides utilities for working with its name and coordinates.
    """

    def __init__(self, city: str, location: Coordinates) -> None:
        """
        Initialize the location with a city name and coordinates.

        :param city: The name of the city.
        :param location: A tuple containing latitude and longitude.
        """
        if not isinstance(location, tuple) or len(location) != 2 or not all(isinstance(coord, (int, float)) for coord in location):
            raise ValueError("location must be a tuple of two numeric values (latitude, longitude)")

        self.city = city
        self.location = location

    def city_as_filename(self) -> str:
        """
        Convert the city name to a filesystem-friendly filename.

        :return: The city name in lowercase, with spaces replaced by hyphens
                 and punctuation removed.
        """
        return re.sub(r"[^\w-]", "", self.city.lower().replace(" ", "-"))
