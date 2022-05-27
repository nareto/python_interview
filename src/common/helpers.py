from enum import Enum, auto
from typing import Set, List


class ParserStates(Enum):
    inword = auto()
    inpunct = auto()
    inwhitespace = auto()


def split_text(text: str, punct: Set[str]) -> List[str]:
    def get_new_state(char: str) -> ParserStates:
        if char == " ":
            return ParserStates.inwhitespace
        elif char in punct:
            return ParserStates.inpunct
        else:
            return ParserStates.inword

    cur_state = ParserStates.inwhitespace
    word_start_idx = 0
    out = []
    for cur_idx, cur_char in enumerate(text + " "):
        new_state = get_new_state(cur_char)
        if new_state != cur_state:
            if cur_state != ParserStates.inwhitespace:
                out.append(text[word_start_idx:cur_idx].strip(" "))
                word_start_idx = cur_idx
        cur_state = new_state
    print(f"split_text returning: {out}")
    return out
