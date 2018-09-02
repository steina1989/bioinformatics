# Algorithms in Bioinformatics (TÖL504M fall 2018)

This repository contains solutions to the bioinformatics CS course @ University of Iceland.

Functions are defined in bioutils.py and subdirectories contain datasets and main.py program that solve the given assignment, based on IO parameters per each [Rosalind](https://rosalind.info) excercise.


## Run an excercise
```bash
cd x_name_of_excercise
./main.py < rosalind_data_set.txt
```
Note: You will need to export PYTHONPATH environment variable to the project's root directory, before running any main.py that imports bioutils.py

In repository root directory do:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

## Run tests
In repository root directory do:
```bash
./bioutils
```