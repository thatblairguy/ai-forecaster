import unittest
from persona import Persona


class TestPersona(unittest.TestCase):
    """Unit tests for the Persona class."""

    def test_valid_persona_creation(self):
        """Test that a Persona can be created with valid inputs."""
        p = Persona("Adventurer", "Casual")
        self.assertEqual(p.description, "Adventurer")
        self.assertEqual(p.style, "Casual")

    def test_empty_description_raises_error(self):
        """Test that an empty description raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Persona("", "Casual")
        self.assertEqual(str(context.exception), "Persona description must not be empty.")

    def test_empty_style_raises_error(self):
        """Test that an empty style raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Persona("Adventurer", "")
        self.assertEqual(str(context.exception), "Writing style must not be empty.")

    def test_whitespace_only_description_raises_error(self):
        """Test that a description with only whitespace raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Persona("   ", "Casual")
        self.assertEqual(str(context.exception), "Persona description must not be empty.")

    def test_whitespace_only_style_raises_error(self):
        """Test that a style with only whitespace raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Persona("Adventurer", "   ")
        self.assertEqual(str(context.exception), "Writing style must not be empty.")

    def test_properties_return_correct_values(self):
        """Test that the property methods return the correct values."""
        p = Persona("Scholar", "Formal")
        self.assertEqual(p.description, "Scholar")
        self.assertEqual(p.style, "Formal")


if __name__ == "__main__":
    unittest.main()
