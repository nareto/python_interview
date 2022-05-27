# Python interview
This repository is used to test various python skills.

Different branches contain different exercises.

# Test 1
The goal of this program is to tokenize text. That is, given an input string like this:

```txt
Hi! I am me. This is, me (not very interesting I know).
```

it should output a dictionary like this:

```python
{
    "HI": 0,
    "!": 1,
    "I": 2,
    "AM": 3,
    "ME": 4,
    ".": 5,
    "THIS": 6,
    "IS": 7,
    "(": 8,
    "NOT": 9,
    "VERY": 10,
    "INTERESTING": 11,
    "KNOW": 12,
    ")": 13
}
```

In `src/common/tokenizer.py` the class `Tokenizer` is defined