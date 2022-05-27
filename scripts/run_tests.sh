#!/bin/bash

pytest src/tests/*.py "${@}" -s

#to drop into pdb on an exception use the following instead:
# pytest src/tests/*.py "${@}" --pdb  -sx