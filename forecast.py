import asyncio
import random
from datetime import datetime
from zoneinfo import ZoneInfo

import lib.config
from lib.generator import Generator
from lib.weather import Weather


async def main():

    async def get_text(personality, location):

        weather = await weather_gen.get_forecast(location)

        prompt = (
            f"You are a(n) {personality.description}.\n"
            f"Using the below WEATHERDATA, compose a report in the DESIGNATEDSTYLE\n"
            f"Do not include any extra notes/text.\n"
            f"DESIGNATEDSTYLE: {personality.style}\n"
            f"WEATHERDATA: {weather}"
        )

        text = await gen.generate(prompt)

        return text

    # Set the timezone
    eastern = ZoneInfo("America/New_York")

    # Run multiple concurrently
    semaphore = asyncio.Semaphore(3)

    async def process_location(loc):
        """Process a single location."""
        async with semaphore:

            # Get the current time in Eastern Time
            now = datetime.now(eastern)

            personality = random.choice(config.personalities)
            text = await get_text(personality, loc.location)

            report = f"# Forecast for: {loc.city}\n\n"
            report += now.strftime("Generated on %B %d, %Y at %I:%M%p Eastern Time\n\n")
            report += text
            report += "\n\n---\n"
            report += f"**STYLE:** {personality.style}"

            with open(f'{config.output_location}/{loc.city_as_filename()}.txt', 'w', encoding='utf-8') as file:
                file.write(report)

    config = lib.config.load("config.json")
    if config is None:
        return

    gen = Generator(config.ai.host, config.ai.model)
    weather_gen = Weather(config.email)

    # Use asyncio.gather to run the tasks concurrently
    tasks = [process_location(loc) for loc in config.locations]
    await asyncio.gather(*tasks)

    await weather_gen.close()


if __name__ == "__main__":
    asyncio.run(main())
