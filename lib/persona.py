class Persona:
    """
    Describes a person and their writing style.
    """

    def __init__(self, description: str, style: str) -> None:
        """
        Initialize the object with a description of a person and their
        writing style.

        :param description: A description of a person.
        :param style: A description of their writing style.
        """

        if not description.strip():
            raise ValueError("Persona description must not be empty.")
        if not style.strip():
            raise ValueError("Writing style must not be empty.")

        self._description = description
        self._style = style

    @property
    def description(self) -> str:
        """Get the persona name."""
        return self._description

    @property
    def style(self) -> str:
        """Get the style."""
        return self._style