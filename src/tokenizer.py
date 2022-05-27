from typing import Dict
from src.text_suppliers.text_suppliers import TextSupplier


class Tokenizer():
    def __init__(self, text_supplier: TextSupplier) -> None:
        self.text_supplier = text_supplier

    def tokenize(self) -> Dict:
        text = self.text_supplier.get_text()
        print("text supplier gave this text:", text)
        out = {}
        return out

    