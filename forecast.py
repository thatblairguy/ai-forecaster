import asyncio

import lib.config
from lib.generator import Generator
from lib.weather import Weather


async def main():

    config = lib.config.load("config.json")

    gen = Generator(config.ai.host, config.ai.model)
    weatherGen = Weather(config.email, config.location)

    role = "Shakespearean scholar"
    style = "Shakespearean sonnet"
    weather = await weatherGen.getForecast()

    prompt = (
        f"You are a {role}.\n"
        f"Using the below WEATHERDATA, compose a report in the DESIGNATEDSTYLE\n"
        f"Do not include any extra notes/text.\n"
        f"DESIGNATEDSTYLE: {style}\n"
        f"WEATHERDATA: {weather}"
    )

    text = await gen.generate(prompt)
    print(text)


if __name__ == "__main__":
    asyncio.run(main())
