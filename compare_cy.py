import platform

if platform.system() == 'Windows':
    from test_paths import join_paths, valid_list_paths, rel_paths, norm_paths
else:
    from unix_test_paths import paths, join_paths, list_paths, rel_paths, norm_paths, valid_list_paths

import timeit
import faster_os
import faster_os_cy
import os


def test_funcs_pair(pair, number=5000):
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


funcs_to_test = [
    (
        'split',
        faster_os_cy.split,
        faster_os.split,
    ),
    (
        'splitdrive',
        faster_os_cy.splitdrive,
        faster_os.splitdrive,
    ),
    (
        'normcase',
        faster_os_cy.normcase,
        faster_os.normcase,
    ),
    (
        'splitext',
        faster_os_cy.splitext,
        faster_os.splitext,
    ),
    (
        'join',
        faster_os_cy.join,
        faster_os.join,
        join_paths,
        True,
    ),
    (
        'relpath',
        faster_os_cy.relpath,
        faster_os.relpath,
        rel_paths,
        True,
    ),
    (
        'ismount',
        faster_os_cy.ismount,
        faster_os.ismount,
    ),
    (
        'normpath',
        faster_os_cy.normpath,
        faster_os.normpath,
        norm_paths,
        False,
    ),
    (
        'expanduser',
        faster_os_cy.expanduser,
        faster_os.expanduser,
    ),
    (
        'abspath',
        faster_os_cy.abspath,
        faster_os.abspath,
    ),
    (
        'isabs',
        faster_os_cy.isabs,
        faster_os.isabs,
    ),
    (
        'basename',
        faster_os_cy.basename,
        faster_os.basename,
    ),
    (
        'dirname',
        faster_os_cy.dirname,
        faster_os.dirname,
    ),
    (
        'commonpath',
        faster_os_cy.commonpath,
        faster_os.commonpath,
        valid_list_paths,
        False,
    ),
    (
        'commonprefix',
        faster_os_cy.commonprefix,
        faster_os.commonprefix,
        valid_list_paths,
        False,
    ),
]


def os_multi_split(paths):
    splitted = [os.path.split(path) for path in paths]


def multi_split(paths):
    splitted = [faster_os.split(path) for path in paths]


def cy_multi_split(paths):
    splitted = [faster_os_cy.split(path) for path in paths]


def cy_integ_split(paths):
    splitted = faster_os_cy.multi_split(paths)


p = paths * 100000

print('os loop', timeit.timeit(lambda: os_multi_split(p), number=5))
print('py loop', timeit.timeit(lambda: multi_split(p), number=5))
print('cy loop', timeit.timeit(lambda: cy_multi_split(p), number=5))
print('cy multi', timeit.timeit(lambda: cy_integ_split(p), number=5))
"""
for pair in funcs_to_test:
    os_time, faster_os_time = test_funcs_pair(pair, number=1)

for pair in funcs_to_test:
    os_time, faster_os_time = test_funcs_pair(pair)

    print(
        f'\n--> Comparing "{pair[0]}":\nFasterOS is {round(faster_os_time / os_time * 100)}% faster!'
    )
"""
