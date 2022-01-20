import platform

if platform.system() == 'Windows':
    from win.test_paths import join_paths, valid_list_paths, rel_paths, norm_paths
else:
    from unix.test_paths import paths, join_paths, list_paths, rel_paths, norm_paths, valid_list_paths

import timeit
import faster_os
import faster_os_py
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


cy_vs_os = [
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

cy_vs_py = [
    (
        'split',
        faster_os_py.split,
        faster_os.split,
    ),
    (
        'splitdrive',
        faster_os_py.splitdrive,
        faster_os.splitdrive,
    ),
    (
        'normcase',
        faster_os_py.normcase,
        faster_os.normcase,
    ),
    (
        'splitext',
        faster_os_py.splitext,
        faster_os.splitext,
    ),
    (
        'join',
        faster_os_py.join,
        faster_os.join,
        join_paths,
        True,
    ),
    (
        'relpath',
        faster_os_py.relpath,
        faster_os.relpath,
        rel_paths,
        True,
    ),
    (
        'ismount',
        faster_os_py.ismount,
        faster_os.ismount,
    ),
    (
        'normpath',
        faster_os_py.normpath,
        faster_os.normpath,
        norm_paths,
        False,
    ),
    (
        'expanduser',
        faster_os_py.expanduser,
        faster_os.expanduser,
    ),
    (
        'abspath',
        faster_os_py.abspath,
        faster_os.abspath,
    ),
    (
        'isabs',
        faster_os_py.isabs,
        faster_os.isabs,
    ),
    (
        'basename',
        faster_os_py.basename,
        faster_os.basename,
    ),
    (
        'dirname',
        faster_os_py.dirname,
        faster_os.dirname,
    ),
    (
        'commonpath',
        faster_os_py.commonpath,
        faster_os.commonpath,
        valid_list_paths,
        False,
    ),
    (
        'commonprefix',
        faster_os_py.commonprefix,
        faster_os.commonprefix,
        valid_list_paths,
        False,
    ),
    (
        'multi_split',
        faster_os_py.multi_split,
        faster_os.multi_split,
        valid_list_paths,
        False,
    ),
]

cy_vs_os
cy_vs_py
funcs_to_test = cy_vs_os

for pair in funcs_to_test:
    os_time, faster_os_time = test_funcs_pair(pair, number=1)

for pair in funcs_to_test:
    os_time, faster_os_time = test_funcs_pair(pair)

    print(
        f'\n--> Comparing "{pair[0]}":\nFasterOS is {round(os_time / faster_os_time * 100)}% faster!'
    )
