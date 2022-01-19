import platform

if platform.system() == 'Windows':
	from test_paths import join_paths, valid_list_paths, rel_paths, norm_paths
else:
	from unix_test_paths import paths, join_paths, list_paths, rel_paths, norm_paths, valid_list_paths

import timeit
import faster_os_cy as faster_os
#import faster_os
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
        os.path.split,
        faster_os.split,
    ),
    (
        'splitdrive',
        os.path.splitdrive,
        faster_os.splitdrive,
    ),
    (
        'normcase',
        os.path.normcase,
        faster_os.normcase,
    ),
    (
        'splitext',
        os.path.splitext,
        faster_os.splitext,
    ),
    (
        'join',
        os.path.join,
        faster_os.join,
        join_paths,
        True,
    ),
    (
        'relpath',
        os.path.relpath,
        faster_os.relpath,
        rel_paths,
        True,
    ),
    (
        'ismount',
        os.path.ismount,
        faster_os.ismount,
    ),
    (
        'normpath',
        os.path.normpath,
        faster_os.normpath,
        norm_paths,
        False,
    ),
    (
        'expanduser',
        os.path.expanduser,
        faster_os.expanduser,
    ),
    (
        'abspath',
        os.path.abspath,
        faster_os.abspath,
    ),
    (
        'isabs',
        os.path.isabs,
        faster_os.isabs,
    ),
    (
        'basename',
        os.path.basename,
        faster_os.basename,
    ),
    (
        'dirname',
        os.path.dirname,
        faster_os.dirname,
    ),
    (
        'commonpath',
        os.path.commonpath,
        faster_os.commonpath,
        valid_list_paths,
        False,
    ),
    (
        'commonprefix',
        os.path.commonprefix,
        faster_os.commonprefix,
        valid_list_paths,
        False,
    ),
]


for pair in funcs_to_test:
    os_time, faster_os_time = test_funcs_pair(pair, number=1)

for pair in funcs_to_test:
    os_time, faster_os_time = test_funcs_pair(pair)

    print(
        f'\n--> Comparing "{pair[0]}":\nFasterOS is {round(os_time / faster_os_time * 100)}% faster!'
    )
