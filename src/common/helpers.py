from typing import Set, List

def multisplit_text(text: str, punct: Set[str]) -> List[str]:
    raw_splits = text.split(" ")
    splits = []
    for word in raw_splits:
        stripped_word = word.strip("".join(punct))
        if word != stripped_word:
            splits.append(stripped_word)
            splits.append(word[len(stripped_word):])
        else:
            splits.append(word)
    return splits