import multiprocessing
from random import choice, random, randrange
import threading
import time
import asyncio

# const
NUMBER_COUNT = 100_000_000
THREAD_COUNT = 100
MULTITHREAD_EXECUTIONS_COUNT = int(NUMBER_COUNT / THREAD_COUNT)

# PROCESS_COUNT = 4
PROCESS_COUNT = multiprocessing.cpu_count()
PROCESS_EXECUTIONS_COUNT = int(NUMBER_COUNT / PROCESS_COUNT)

# compared functions


def count_choices_choice(iter_number):
    variants = ['yes', 'no']
    yes = 0
    no = 0
    for _ in range(iter_number):
        result = choice(variants)
        if result == 'no':
            no += 1
        else:
            yes += 1
    return yes, no


def count_choices_random(iter_number):
    yes = 0
    no = 0
    for _ in range(iter_number):
        result = random() < 0.5
        if result:
            no += 1
        else:
            yes += 1
    return yes, no

async def count_choices_random_async(iter_number):
    yes = 0
    no = 0
    for _ in range(iter_number):
        result = random() < 0.5
        if result:
            no += 1
        else:
            yes += 1
    return yes, no


def count_choices_randrange(iter_number):
    total = 0
    yes = 0
    for _ in range(iter_number):
        result = randrange(2)
        total += 1
        yes += result

    no = total - yes
    return yes, no


# executions


def single_threaded(func, name=''):
    start = time.time()
    yes_single, no_single = func(NUMBER_COUNT)
    end = time.time()
    return f'Single-threaded {name}: {end - start:.2f} sec\nyes: {yes_single}, no: {no_single}'


def multi_threaded(func, name=''):
    lock = threading.Lock()
    start = time.time()

    threads = []
    results = []
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=lambda: results.append(
            func(MULTITHREAD_EXECUTIONS_COUNT)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    yes_multi = sum(yes for yes, _ in results)
    no_multi = sum(no for _, no in results)

    end = time.time()
    return f'Multi-threaded {name}: {end - start:.2f} sec\nyes: {yes_multi}, no: {no_multi}'


def multi_process(func, name=''):
    start = time.time()

    with multiprocessing.Pool(processes=PROCESS_COUNT) as pool:
        results = pool.map(func, [PROCESS_EXECUTIONS_COUNT] * PROCESS_COUNT)

    yes_multi = sum(yes for yes, _ in results)
    no_multi = sum(no for _, no in results)

    end = time.time()
    return f'Multi-processing {name}: {end - start:.2f} sec\nyes: {yes_multi}, no: {no_multi}'


async def call_func(func, name=''):
    start = time.time()
    results = await func(NUMBER_COUNT)
    #yes_multi = sum(yes for yes, _ in results)
    #no_multi = sum(no for _, no in results)
    yes_multi, no_multi = results

    end = time.time()
    # result = f'Multi-processing {name}: {end - start:.2f} sec\nyes: {yes_multi}, no: {no_multi}'
    # print(result)
    return f'Async {name}: {end - start:.2f} sec\nyes: {yes_multi}, no: {no_multi}'

if __name__ == '__main__':

    # functions = (count_choices_choice, count_choices_randrange, count_choices_random)
    # modes = ('single_threaded', 'multi_threaded', 'multi_process')

    # for mode in modes:
    #     print(f"\n{mode.title()} Execution:")
    #     for function in functions:
    #         func_name = function.__name__.replace('_', ' ').title()  # Format name for clarity
    #         print(f"- {func_name}:")
    #         print(globals()[mode](function, func_name))  # Dynamically call mode function

    #     if mode == 'multi_process':
    #         print(f"CPU count: {multiprocessing.cpu_count()}")  # Print CPU count once

    # Single-threaded execution
    print(single_threaded(count_choices_choice, 'choice'))
    print(single_threaded(count_choices_randrange, 'randrange'))
    print(single_threaded(count_choices_random, 'random'))
    print()

    # Multi-threaded execution
    print(multi_threaded(count_choices_choice, 'choice'))
    print(multi_threaded(count_choices_randrange, 'randrange'))
    print(multi_threaded(count_choices_random, 'random'))
    print()

    # Multi-processing execution
    print(f'CPU count: {PROCESS_COUNT}')
    print(multi_process(count_choices_choice, 'choice'))
    print(multi_process(count_choices_randrange, 'randrange'))
    print(multi_process(count_choices_random, 'random'))
    print()

    print('async')
    output = asyncio.run(call_func(count_choices_random_async, 'random async'))
    print(output)
    
    