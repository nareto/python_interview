from .text_suppliers import TextSupplier
import requests

class DownloadTextSupplier(TextSupplier):
    def __init__(self, url: str) -> None:
        self.url = url
        super().__init__

    def get_text(self) -> str:
        response = requests.get(self.url)
        return response.text

    