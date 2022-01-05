import logging

class Generate:
    def __init__(self, json_data) -> None:
        self.prompt = json_data["prompt"]
        self.length = json_data["length"]

    def check(self) -> bool:
        try:
            if len(self.prompt) > 0 < 1000 \
            and int(self.length) >= 5 <= 60:
                return True
        except Exception as e:
            logging.warning(
                "Middleware \"generate\" method check error: %s" % e)
        finally:
            return False
