

## Random Selection Speed Execution Script (CPU-bound tasks)

### Overview

This script compares the performance of different methods for randomly selecting between two options ("yes" and "no") a massive number of times. It evaluates three core methods:

* `choice` function with a pre-defined list of options
* `randrange` function to generate a random integer (0 or 1)
* `random` function to generate a random float (less than 0.5 for "no", greater than or equal to 0.5 for "yes")

The script executes these methods in three different environments:

* Single-threaded
* Multi-threaded
* Multi-processing

This allows for a comprehensive comparison of performance across various execution models.

### Features

* Compares three random selection methods: `choice`, `randrange`, `random`
* Supports single-threaded, multi-threaded, and multi-processing execution
* Calculates the execution time and outcome distribution (number of "yes" and "no" selections)

### Installation

This script requires the following Python libraries:

* `multiprocessing`
* `random`
* `threading`
* `asyncio` (for the asynchronous execution)

These libraries are typically included in the standard Python installation. You can verify and install them using the `pip` package manager:

```bash
pip install -r requirements.txt
```


### Usage

1. Save the script as `random_select.py`.
2. Run the script from your terminal:

```bash
python random_select.py
```

The script will automatically execute the comparison and display the results for each method and execution mode.

### Technologies Used

* Python programming language
* `multiprocessing` library for parallel processing
* `threading` library for multi-threaded execution
* `random` library for generating random values
* `asyncio` library for asynchronous programming (used for the asynchronous execution)


<details>

<summary>Execution Results (click tio expand)</summary>

**Mac with M1**

```
Single-threaded choice: 23.19 sec
yes: 50005287, no: 49994713
Single-threaded randrange: 21.13 sec
yes: 49997033, no: 50002967
Single-threaded random: 5.62 sec
yes: 50004773, no: 49995227

Multi-threaded choice: 23.73 sec
yes: 49999124, no: 50000876
Multi-threaded randrange: 21.30 sec
yes: 50004134, no: 49995866
Multi-threaded random: 5.51 sec
yes: 50004663, no: 49995337

CPU count: 8
Multi-processing choice: 4.85 sec
yes: 49999987, no: 50000013
Multi-processing randrange: 4.39 sec
yes: 50009667, no: 49990333
Multi-processing random: 1.27 sec
yes: 50003205, no: 49996795

async
Async random async: 5.51 sec
yes: 49995906, no: 50004094
```

**Windows 11 on Intel i5-8500T**

```
Single-threaded choice: 41.88 sec
yes: 50000746, no: 49999254
Single-threaded randrange: 44.21 sec
yes: 50003825, no: 49996175
Single-threaded random: 11.41 sec
yes: 50004322, no: 49995678

Multi-threaded choice: 40.88 sec
yes: 49999690, no: 50000310
Multi-threaded randrange: 43.36 sec
yes: 49995894, no: 50004106
Multi-threaded random: 11.46 sec
yes: 50003137, no: 49996863

CPU count: 6
Multi-processing choice: 9.69 sec
yes: 50008809, no: 49991187
Multi-processing randrange: 10.34 sec
yes: 49989394, no: 50010602
Multi-processing random: 2.85 sec
yes: 49995572, no: 50004424

async
Async random async: 11.40 sec
yes: 49996877, no: 50003123
```


**Python 3.11.8 on Ubuntu 22.04 with Intel i5-8500T**

```
Single-threaded choice: 29.56 sec
yes: 49997575, no: 50002425
Single-threaded randrange: 31.43 sec
yes: 49996034, no: 50003966
Single-threaded random: 7.87 sec
yes: 50010426, no: 49989574

Multi-threaded choice: 42.30 sec
yes: 49991732, no: 50008268
Multi-threaded randrange: 44.60 sec
yes: 50000429, no: 49999571
Multi-threaded random: 9.05 sec
yes: 50008182, no: 49991818

CPU count: 6
Multi-processing choice: 5.83 sec
yes: 50009441, no: 49990555
Multi-processing randrange: 6.17 sec
yes: 50006118, no: 49993878
Multi-processing random: 1.48 sec
yes: 50009849, no: 49990147

async
Async random async: 7.94 sec
yes: 49992179, no: 50007821
```
</details>
