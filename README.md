# Python interview
This repository is used to test various python skills.

Different branches contain different exercises.

# Task
The goal of this program is to tokenize text. That is, given an input string like this:

```txt
Some text. And .more.
```

it should output a dictionary like this:

```python
{"SOME": 1, "TEXT": 1, ".": 3, "AND": 1, "MORE": 1}
```

In `src/tests` there are pytest tests - you can run them by running the script `scripts/run_tests.sh`. Tests2 and 3 are not passing: fix the code accordingly.