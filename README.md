

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


## Results

This table summarizes the execution times for the "multi-processing random" selection method across various environments:

| Environment | Multi-processing (random)          |
|---|------------------------------------|
| Python 3.11.7 on Mac with M1 | 1.27 sec |
| Python 3.11.7 on Windows 11 with Intel i5-8500T (Cores/Logical CPU: 6) | 2.39 sec                           |
| Python 3.12.1 on Windows 11 with Intel i5-8500T (Cores/Logical CPU: 6) | 2.21 sec                           |
| Python 3.11.8 on Ubuntu 22.04.4 with Intel i5-8500T (Cores/Logical CPU: 6) | 1.48 sec|
| Python 3.11.7 on Windows 11 with Intel i5-1035G7 (Cores: 4 / Logical CPU: 6) | 4.18 sec |
| Python 3.11.2 on LMDE 6 (Debian 12) with Intel Celeron N3060 (2 cores) | 16.91 sec |
| Python 3.11.8 on Google IDX VM with RAM: 8Gb, Cores: 2 | 12.98 sec |


<details>

<summary>Detailed execution Results (click to expand)</summary>

**Python 3.11.7 on Mac with M1**

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

**Python 3.11.7 on Windows 11 with Intel i5-8500T (Cores/Logical CPU: 6)** - same hardware as below

```
Single-threaded choice: 40.82 sec
yes: 50009297, no: 49990703
Single-threaded randrange: 42.31 sec
yes: 50000790, no: 49999210
Single-threaded random: 10.78 sec
yes: 49992072, no: 50007928

Multi-threaded choice: 40.46 sec
yes: 49994303, no: 50005697
Multi-threaded randrange: 41.79 sec
yes: 50005119, no: 49994881
Multi-threaded random: 10.99 sec
yes: 50003664, no: 49996336

CPU count: 6
Multi-processing choice: 7.56 sec
yes: 49998711, no: 50001285
Multi-processing randrange: 8.14 sec
yes: 49990076, no: 50009920
Multi-processing random: 2.39 sec
yes: 50003991, no: 49996005

async
Async random async: 11.13 sec
yes: 49999728, no: 50000272
```

**Python 3.12.1 on Windows 11 with Intel i5-8500T (Cores/Logical CPU: 6)** - same hardware as below

```
Single-threaded choice: 42.19 sec
yes: 49995497, no: 50004503
Single-threaded randrange: 45.14 sec
yes: 50009001, no: 49990999
Single-threaded random: 10.21 sec
yes: 50003166, no: 49996834

Multi-threaded choice: 41.39 sec
yes: 50003229, no: 49996771
Multi-threaded randrange: 44.09 sec
yes: 50002289, no: 49997711
Multi-threaded random: 10.46 sec
yes: 50000682, no: 49999318

CPU count: 6
Multi-processing choice: 8.43 sec
yes: 49999935, no: 50000061
Multi-processing randrange: 8.88 sec
yes: 50017700, no: 49982296
Multi-processing random: 2.21 sec
yes: 50000743, no: 49999253

async
Async random async: 9.99 sec
yes: 50006008, no: 49993992
```

**Python 3.11.8 on Ubuntu 22.04.4 with Intel i5-8500T (Cores/Logical CPU: 6)** - same hardware as above 

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

**Python 3.11.7 on Windows 11 with Intel i5-1035G7 (Cores: 4 / Logical CPU: 6)** - laptop

```
Single-threaded choice: 32.51 sec
yes: 49996559, no: 50003441
Single-threaded randrange: 34.51 sec
yes: 50009436, no: 49990564
Single-threaded random: 8.52 sec
yes: 49998908, no: 50001092

Multi-threaded choice: 34.70 sec
yes: 50004930, no: 49995070
Multi-threaded randrange: 37.42 sec
yes: 49992683, no: 50007317
Multi-threaded random: 10.67 sec
yes: 49995058, no: 50004942

CPU count: 8
Multi-processing choice: 9.78 sec
yes: 50002242, no: 49997758
Multi-processing randrange: 13.86 sec
yes: 50004650, no: 49995350
Multi-processing random: 4.18 sec
yes: 50014722, no: 49985278

async
Async random async: 8.99 sec
yes: 50004017, no: 49995983
```

**Python 3.11.2 on LMDE 6 (Debian 12) with Intel Celeron N3060 (2 cores)** - netbook

```
Single-threaded choice: 101.13 sec
yes: 50003630, no: 49996370
Single-threaded randrange: 127.73 sec
yes: 50001691, no: 49998309
Single-threaded random: 27.51 sec
yes: 50003751, no: 49996249

Multi-threaded choice: 123.28 sec
yes: 49999168, no: 50000832
Multi-threaded randrange: 158.08 sec
yes: 49997208, no: 50002792
Multi-threaded random: 34.27 sec
yes: 49998846, no: 50001154

CPU count: 2
Multi-processing choice: 65.80 sec
yes: 49998558, no: 50001442
Multi-processing randrange: 65.05 sec
yes: 50002651, no: 49997349
Multi-processing random: 16.91 sec
yes: 50000459, no: 49999541

async
Async random async: 26.28 sec
yes: 50000319, no: 49999681
```

**Python 3.11.8 on Google IDX VM with RAM: 8Gb, Cores: 2**

```
Single-threaded choice: 47.72 sec
yes: 50001776, no: 49998224
Single-threaded randrange: 49.09 sec
yes: 49999663, no: 50000337
Single-threaded random: 12.60 sec
yes: 49997630, no: 50002370

Multi-threaded choice: 51.94 sec
yes: 49997591, no: 50002409
Multi-threaded randrange: 56.82 sec
yes: 50004175, no: 49995825
Multi-threaded random: 12.54 sec
yes: 50006503, no: 49993497

CPU count: 2
Multi-processing choice: 46.28 sec
yes: 49992610, no: 50007390
Multi-processing randrange: 48.74 sec
yes: 50003956, no: 49996044
Multi-processing random: 12.98 sec
yes: 49987894, no: 50012106

async
Async random async: 12.02 sec
yes: 49998566, no: 50001434
```

</details>

### Observations:

* The "multi-processing random" selection method achieves significantly faster execution times compared to single-threaded or multi-threaded approaches (data not shown, but likely in the original table). This is because it utilizes multiple CPU cores for parallel processing, leading to faster completion of the random selection tasks.
* There are variations in performance across different environments. Mac with M1 shows the fastest execution time (1.27 seconds), followed by Ubuntu and various Windows machines with Intel i5 processors (ranging from 1.48 to 4.18 seconds). The slowest execution is observed on the netbook with a Celeron N3060 CPU (16.91 seconds) and the Google IDX VM with limited cores (12.98 seconds).
* These variations can be attributed to several factors:
    * **CPU architecture:** Modern CPUs like M1 are optimized for parallel processing, leading to faster execution.
    * **Number of cores:** More cores allow for more parallel tasks, improving speed.
    * **Overall system performance:** Factors like RAM and storage speed can also influence execution times.

**Overall, the results demonstrate the benefits of multi-processing for random selection tasks. The choice of hardware and system configuration can significantly impact performance.**
