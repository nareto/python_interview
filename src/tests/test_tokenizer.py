from src.text_suppliers.downloadtext_supplier import DownloadTextSupplier
from src.text_suppliers.textfile_supplier import TextFileSupplier
from src.tokenizer import Tokenizer


def test1():
    text_supplier = TextFileSupplier("src/tests/test1_input.txt")
    tokenizer = Tokenizer(text_supplier)
    tokenized_dict = tokenizer.tokenize()
    assert tokenized_dict == {"SOME": 1, "TEXT": 1, ".": 1}


def test2():
    text_supplier = TextFileSupplier("src/tests/test2_input.txt")
    tokenizer = Tokenizer(text_supplier)
    tokenized_dict = tokenizer.tokenize()
    assert tokenized_dict == {
        "SOME": 1,
        "\n": 4,
        "TEXT": 1,
        " ON": 1,
        "MULTIPLE-LINES": 1,
        "!": 1,
    }


# def test3():
#     text_supplier = DownloadTextSupplier("https://archive.org/stream/manualzilla-id-5728017/5728017_djvu.txt")
#     tokenizer = Tokenizer(text_supplier)
#     tokenizer.tokenize()
