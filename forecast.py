import asyncio
import random

import lib.config
from lib.generator import Generator
from lib.weather import Weather


async def main():

    config = lib.config.load("config.json")

    gen = Generator(config.ai.host, config.ai.model)
    weatherGen = Weather(config.email, config.location)

    personality = random.choice(config.personalities)
    weather = await weatherGen.getForecast()

    prompt = (
        f"You are a(n) {personality.persona}.\n"
        f"Using the below WEATHERDATA, compose a report in the DESIGNATEDSTYLE\n"
        f"Do not include any extra notes/text.\n"
        f"DESIGNATEDSTYLE: {personality.style}\n"
        f"WEATHERDATA: {weather}"
    )

    text = await gen.generate(prompt)
    print(text)

    print("\n\n---")
    print(f"**STYLE:** {personality.style}")


if __name__ == "__main__":
    asyncio.run(main())
