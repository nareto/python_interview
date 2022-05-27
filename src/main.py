import argparse
import sys
from text_suppliers.downloadtext_supplier import DownloadTextSupplier

from text_suppliers.textfile_supplier import TextFileSupplier
from tokenizer import Tokenizer


def get_parsed_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        usage="%(prog)s <text_supplier> [OPTIONS]",
        description="Tokenize text. <text_supplier> can be either `textfile`,"
        + "in which case --input-file must be the path to a text file,"
        + "or `download`, in which case the text in the url in the --url option will be used",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "text_supplier",
        nargs="?",
        default="textfile",
        help="either ",
    )
    parser.add_argument(
        "--input-file",
        default=None,
        help="path to input textfile",
    )
    parser.add_argument(
        "--url",
        default=None,
        help="url to download text from",
    )
    parsed_args = parser.parse_args()
    if (parsed_args.text_supplier == "textfile" and parsed_args.input_file is None) or (
        parsed_args.text_supplier == "download" and parsed_args.url is None
    ):
        parser.print_help()
        sys.exit(1)
    return parsed_args


def tokenize(parsed_args):
    print("tokenizing...")
    if parsed_args.text_supplier == "textfile":
        text_supplier = TextFileSupplier(parsed_args.input_file)
    elif parsed_args.text_supplier == "download":
        text_supplier = DownloadTextSupplier(parsed_args)
    else:
        sys.exit(1)
    tokenizer = Tokenizer(text_supplier)
    tokenizer.tokenize()

if __name__ == "__main__":
    parsed_args = get_parsed_args()
    tokenize(parsed_args)
