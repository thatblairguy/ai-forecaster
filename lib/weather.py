import aiohttp
from pynws import SimpleNWS, call_with_retry
from typing import Tuple


class Weather:
    """
    Fetch weather reports from the US National Weather Service using pynws.

    :param userid: A string containing the user id (email address) for  authentication.
    """

    def __init__(self, userid: str) -> None:

        if not isinstance(userid, str) or not userid.strip():
            raise ValueError("User ID must be a non-empty string.")

        self.userid = userid
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()  # Clean up the session

    async def get_forecast(self, location: Tuple[float, float]) -> str:
        """
        Get the weather forecast for a specific location.

        :param location: A tuple (latitude, longitude) representing the location.

        :return: A detailed forecast string.
        """

        if not isinstance(location, tuple) or len(location) != 2:
            raise ValueError(
                "Location must be a tuple with two elements: (latitude, longitude)."
            )

        retry_interval = 0.0
        max_retry = 10.0

        nws = SimpleNWS(*location, self.userid, self.session)
        await nws.set_station()
        await call_with_retry(nws.update_observation, retry_interval,  max_retry)
        await call_with_retry(nws.update_forecast, retry_interval,  max_retry)
        await call_with_retry(nws.update_alerts_forecast_zone, retry_interval,  max_retry)
        await call_with_retry(nws.update_detailed_forecast, retry_interval,  max_retry)

        text = nws.forecast[0]["detailedForecast"]

        return text


if __name__ == "__main__":
    print("Not a standalone module.")
