class AISource:
    """
    Contains the information needed for communicating with the AI.
    """

    def __init__(self, host: str, model: str) -> None:
        self._host = host
        self._model = model

    @property
    def host(self) -> str:
        """Get the AI's base URL."""
        return self._host

    @property
    def model(self) -> str:
        """Get the model to load."""
        return self._model


