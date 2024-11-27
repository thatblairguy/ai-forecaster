# AI Forecaster

Silly program to turn the weather forecast into something else via a GPT.

Obtains the current weather from the US National Weather Service API (via [pynws](https://pypi.org/project/pynws/)) and runs it through a local GPT to transform it into a fun format.

## Setup

1. Install [ollama](https://ollama.com/) and install a model.
    - e.g. `ollama install llama3.1:latest`
1. Copy `config.sample.json` to `config.json`.
1. Set the `email` property to your email address (this is needed for the NWS API).
1. Under the `locations` key, create a list of location objects:
    - Set the `city` key to the name state of a city.
    - Set `latitude` and `longitude` to the coordinates of the city.
    - Repeat for any additional cities.
1. Under the `ai` key, set `server` to the system where ollama is installed.
    - If ollama is not installed on the same machine as the AI Forecaster program, you'll need to [configure ollama to accept external connections](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-do-i-configure-ollama-server)
1. Under the `ai` key, set `model` to the same model that was installed in step 1.

The `personalities` key is an array of "personality" objects.  For an individual object, the `persona` key describes the type of "person" the AI is impersonating (e.g. "Shakespearean scholar") and the `style` key is the writing style to use (e.g. "Shakespearean sonnet").
