from translatepy import Translator
from requests import post

class Story:
    def __init__(self, prompt: str, length: int = 25) -> None:
        self.url = "https://pelevin.gpt.dobro.ai/generate"
        self.prompt = prompt; self.length = length

    def request(self, prompt: str) -> dict or None:
        resp = post(self.url, json={
            "prompt": prompt, "length": self.length
        })
        if resp.status_code >= 200 < 400: return resp.json()

    @staticmethod
    def translate_array(array: list, lang: str = "Ukrainian") -> list or None:
        return [Translator().translate(el, lang).result for el in array]

    @staticmethod
    def translate(string: str, lang: str = "Ukrainian") -> str or None:
        return Translator().translate(string, lang).result

    def get(self) -> str:
        ru_in = self.translate(self.prompt, "Russian")
        ru_array = self.request(ru_in)
        return self.translate_array(ru_array)
