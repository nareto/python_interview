from typing import Dict, List, Set
from src.text_suppliers.text_suppliers import TextSupplier
from src.common.helpers import split_text

PUNCT = {"!", ".", " ", "\n"}


class Tokenizer:
    def __init__(self, text_supplier: TextSupplier) -> None:
        self.text_supplier = text_supplier

    def tokenize(self) -> Dict:
        text = self.text_supplier.get_text()
        out = {}
        for word in split_text(text=text, punct=PUNCT):
            wupper = word.upper()
            if wupper not in out:
                out[wupper] = 0
            out[wupper] += 1
        return out
