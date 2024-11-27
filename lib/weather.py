import aiohttp
import pynws


class Weather:

    def __init__(self, userid: str) -> None:
        self.userid = userid
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()  # Clean up the session

    async def get_forecast(self, location: tuple) -> str:

        if not isinstance(location, tuple) or len(location) != 2:
            raise ValueError(
                "Location must be a tuple with two elements: (latitude, longitude)."
            )

        nws = pynws.SimpleNWS(*location, self.userid, self.session)
        await nws.set_station()
        await nws.update_observation()
        await nws.update_forecast()
        await nws.update_alerts_forecast_zone()
        await nws.update_detailed_forecast()
        # print(nws.observation)
        # print(nws.forecast[0])
        # print(nws.alerts_forecast_zone)
        # pprint(nws.detailed_forecast.get_details_for_time(date))
        # pprint(date)

        text = nws.forecast[0]["detailedForecast"]

        return text


if __name__ == "__main__":
    print("Not a standalone module.")
