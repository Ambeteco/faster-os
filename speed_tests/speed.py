import timeit
import os


def test_funcs_pair(pair, number=100):
    def wrapper(func, unpack=False):
        if unpack:
            return lambda: [func(*path) for path in paths]
        return lambda: [func(path) for path in paths]

    unpack = False

    if len(pair) == 3:
        paths = [
            '', 'C:', 'C:1', '\\\\machine\\mountpoint\\directory\\etc\\',
            '\\\\host-name\\share-name\\file_path',
            'C:\\hello world\\some path', 'C:\\1\\123/123/123\\123', 'C:\\',
            'C:\\hello world\\some path\\', 'C',
            '\\\\host-name\\share-name\\some\\long\\file\\path'
        ]
    else:
        *pair, paths, unpack = pair

    name, os_func, faster_os_func = pair

    os_time = timeit.timeit(wrapper(os_func, unpack=unpack), number=number)
    faster_os_time = timeit.timeit(wrapper(faster_os_func, unpack=unpack),
                                   number=number)

    return os_time, faster_os_time


def test_funcs_pair_multi(pair, number=1):
    def wrapper(func, unpack=False):
        if unpack:
            return lambda: [func(*path) for path in paths]
        return lambda: [func(path) for path in paths]

    unpack = False

    if len(pair) == 5:
        *pair, unpack = pair

    name, os_func, faster_os_func, paths = pair
    paths *= 3

    os_time = timeit.timeit(wrapper(os_func, unpack=unpack), number=number)
    faster_os_time = timeit.timeit(lambda: faster_os_func(paths),
                                   number=number)

    return os_time, faster_os_time


def compare(funcs_to_test):
    for pair in funcs_to_test:
        os_time, faster_os_time = test_funcs_pair(pair, number=1)

    for pair in funcs_to_test:
        os_time, faster_os_time = test_funcs_pair(pair)

        print(
            f'\n--> Comparing "{pair[0]}":\nFasterOS is {round(os_time / faster_os_time * 100)}% faster!'
        )


def compare_multi(funcs_to_test):
    # for pair in funcs_to_test:
    #     os_time, faster_os_time = test_funcs_pair_multi(pair, number=1)

    for pair in funcs_to_test:
        os_time, faster_os_time = test_funcs_pair_multi(pair)

        print(
            f'\n--> Comparing "{pair[0]}":\nFasterOS is {round(os_time / faster_os_time * 100)}% faster!'
        )
