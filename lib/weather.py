import aiohttp
import pynws


class Weather:

    def __init__(self, userid: str, location: tuple) -> None:
        self.userid = userid
        self.location = location

    async def getForecast(self) -> str:
        async with aiohttp.ClientSession() as session:

            nws = pynws.SimpleNWS(*self.location, self.userid, session)
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
