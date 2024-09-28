import ollama


class Generator:

    def __init__(self, host: str, model_name: str) -> None:
        self.model_name = model_name
        # self.client = ollama.Client(host=host)
        self.client = ollama.AsyncClient(host=host)

    async def generate(self, prompt: str) -> str:
        reply = await self.client.generate(model=self.model_name, prompt=prompt)
        return reply["response"]


if __name__ == "__main__":
    print("Not a standalone module.")
