from .text_suppliers import TextSupplier

class TextFileSupplier(TextSupplier):
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        super().__init__

    def get_text(self) -> str:
        with open(self.filepath, 'r') as f:
            text = f.read()
        return text