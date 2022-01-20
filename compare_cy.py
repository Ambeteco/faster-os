import platform

if platform.system() == 'Windows':
    from win.test_paths import paths, join_paths, valid_list_paths, rel_paths, norm_paths
else:
    from unix.test_paths import paths, join_paths, list_paths, rel_paths, norm_paths, valid_list_paths

import timeit
import faster_os_py
import faster_os
import os


def os_multi_split(paths):
    splitted = [os.path.split(path) for path in paths]


def multi_split(paths):
    splitted = [faster_os_py.split(path) for path in paths]


def cy_multi_split(paths):
    splitted = [faster_os.split(path) for path in paths]


def cy_integ_split(paths):
    splitted = faster_os.multi_split(paths)


p = paths * 100000

print('os loop', timeit.timeit(lambda: os_multi_split(p), number=1))
print('py loop', timeit.timeit(lambda: multi_split(p), number=1))
print('cy loop', timeit.timeit(lambda: cy_multi_split(p), number=1))
print('cy multi', timeit.timeit(lambda: cy_integ_split(p), number=1))
"""
for pair in funcs_to_test:
    os_time, faster_os_time = test_funcs_pair(pair, number=1)

for pair in funcs_to_test:
    os_time, faster_os_time = test_funcs_pair(pair)

    print(
        f'\n--> Comparing "{pair[0]}":\nFasterOS is {round(faster_os_time / os_time * 100)}% faster!'
    )
"""
