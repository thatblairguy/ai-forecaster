import unittest
from location import Coordinates, Location


class TestCoordinates(unittest.TestCase):
    def test_coordinates_initialization(self):
        """
        Test that Coordinates initializes correctly with valid latitude and longitude.
        """
        coords = Coordinates(latitude=39.0, longitude=-77.0)
        self.assertEqual(coords.latitude, 39.0)
        self.assertEqual(coords.longitude, -77.0)


class TestLocation(unittest.TestCase):
    def test_location_initialization_valid(self):
        """
        Test that Location initializes correctly with valid city and coordinates.
        """
        coords = Coordinates(latitude=39.0, longitude=-77.0)
        loc = Location(city="Gaithersburg, MD", location=coords)
        self.assertEqual(loc.city, "Gaithersburg, MD")
        self.assertEqual(loc.location.latitude, 39.0)
        self.assertEqual(loc.location.longitude, -77.0)

    def test_location_initialization_invalid(self):
        """
        Test that Location raises a ValueError with invalid coordinates.
        """
        with self.assertRaises(ValueError):
            Location(city="Invalid City", location=(39.0,))  # Missing longitude
        with self.assertRaises(ValueError):
            Location(city="Invalid City", location=("latitude", -77.0))  # Non-numeric latitude
        with self.assertRaises(ValueError):
            Location(city="Invalid City", location=(39.0, -77.0, 100))  # Extra values in tuple

    def test_city_as_filename(self):
        """
        Test the city_as_filename method for expected output.
        """
        loc = Location(city="Gaithersburg, MD", location=Coordinates(latitude=39.0, longitude=-77.0))
        self.assertEqual(loc.city_as_filename(), "gaithersburg-md")

        loc = Location(city="New York, NY", location=Coordinates(latitude=40.7128, longitude=-74.0060))
        self.assertEqual(loc.city_as_filename(), "new-york-ny")

        loc = Location(city="Los Angeles, CA", location=Coordinates(latitude=34.0522, longitude=-118.2437))
        self.assertEqual(loc.city_as_filename(), "los-angeles-ca")

    def test_city_as_filename_edge_cases(self):
        """
        Test the city_as_filename method with edge cases.
        """
        loc = Location(city="", location=Coordinates(latitude=39.0, longitude=-77.0))
        self.assertEqual(loc.city_as_filename(), "")

        loc = Location(city="123 Main St.", location=Coordinates(latitude=39.0, longitude=-77.0))
        self.assertEqual(loc.city_as_filename(), "123-main-st")


if __name__ == "__main__":
    unittest.main()
