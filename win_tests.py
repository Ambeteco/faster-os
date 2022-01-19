import traceback
from test_paths import paths, join_paths, list_paths, rel_paths, norm_paths, valid_list_paths
import os
import faster_os


def split_test():
    return base_test(os.path.split, faster_os.split, paths)


def splitdrive_test():
    return base_test(os.path.splitdrive, faster_os.splitdrive, paths)


def commonpath_test():
    return base_test(os.path.commonpath, faster_os.commonpath,
                     valid_list_paths)


def commonprefix_test():
    return base_test(os.path.commonprefix, faster_os.commonprefix, list_paths)


def normcase_test():
    return base_test(os.path.normcase, faster_os.normcase, paths)


def abspath_test():
    return base_test(os.path.abspath, faster_os.abspath, paths)


def normpath_test():
    return base_test(os.path.normpath, faster_os.normpath, norm_paths)


def basename_test():
    return base_test(os.path.basename, faster_os.basename, paths)


def ismount_test():
    return base_test(os.path.ismount, faster_os.ismount, paths)


def dirname_test():
    return base_test(os.path.dirname, faster_os.dirname, paths)


def expanduser_test():
    return base_test(os.path.expanduser, faster_os.expanduser, paths)


def relpath_test():
    return base_test(os.path.relpath,
                     faster_os.relpath,
                     rel_paths,
                     unpack=True)


def isabs_test():
    return base_test(os.path.isabs, faster_os.isabs, paths)


def splitext_test():
    return base_test(os.path.splitext, faster_os.splitext, paths)


def join_test():
    return base_test(os.path.join, faster_os.join, join_paths, unpack=True)


def base_test(os_func, faster_os_func, paths, unpack=False):
    fails = 0

    for path in paths:
        if unpack:
            try:
                os_func_result = os_func(*path)
            except:
                print('OS crashed', path, traceback.format_exc())
                continue

            faster_os_func_result = faster_os_func(*path)

        else:
            try:
                os_func_result = os_func(path)
            except:
                print('OS crashed', path, traceback.format_exc())
                continue

            faster_os_func_result = faster_os_func(path)

        if os_func_result != faster_os_func_result:
            print(f'\n\nEquality "{path}":')
            print(f'       os_func: {os_func_result}')
            print(f'faster_os_func: {faster_os_func_result}')

            if type(faster_os_func_result) != type(os_func_result):
                print(f'\ntype: {type(os_func_result)}')
                print(f'type: {type(faster_os_func_result)}\n\n')

            fails += 1

    if fails:
        print(f'Failed {fails}/{len(paths)} tests.')
        return False

    print('Successfully passed this test')
    return True


tests = [
    ('split', split_test),
    ('splitdrive', splitdrive_test),
    ('ismount', ismount_test),
    ('normpath', normpath_test),
    ('abspath', abspath_test),
    ('expanduser', expanduser_test),
    ('relpath', relpath_test),
    ('normcase', normcase_test),
    ('isabs', isabs_test),
    ('join', join_test),
    ('basename', basename_test),
    ('dirname', dirname_test),
    ('commonpath', commonpath_test),
    ('commonprefix', commonprefix_test),
    ('splitext', splitext_test),
    ('relpath', relpath_test),
]
