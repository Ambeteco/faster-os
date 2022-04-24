import traceback
from win.test_paths import paths, join_paths, list_paths, rel_paths, norm_paths, valid_list_paths
import os
import faster_os


def split_test():
    return base_test(os.path.split, faster_os.path.split, paths)


def splitdrive_test():
    return base_test(os.path.splitdrive, faster_os.path.splitdrive, paths)


def commonpath_test():
    return base_test(os.path.commonpath, faster_os.path.commonpath,
                     valid_list_paths)


def commonprefix_test():
    return base_test(os.path.commonprefix, faster_os.path.commonprefix,
                     list_paths)


def normcase_test():
    return base_test(os.path.normcase, faster_os.path.normcase, paths)


def abspath_test():
    return base_test(os.path.abspath, faster_os.path.abspath, paths)


def normpath_test():
    return base_test(os.path.normpath, faster_os.path.normpath, norm_paths)


def basename_test():
    return base_test(os.path.basename, faster_os.path.basename, paths)


def ismount_test():
    return base_test(os.path.ismount, faster_os.path.ismount, paths)


def dirname_test():
    return base_test(os.path.dirname, faster_os.path.dirname, paths)


def expanduser_test():
    return base_test(os.path.expanduser, faster_os.path.expanduser, paths)


def relpath_test():
    return base_test(os.path.relpath,
                     faster_os.path.relpath,
                     rel_paths,
                     unpack=True)


def isabs_test():
    return base_test(os.path.isabs, faster_os.path.isabs, paths)


def splitext_test():
    return base_test(os.path.splitext, faster_os.path.splitext, paths)


def join_test():
    return base_test(os.path.join,
                     faster_os.path.join,
                     join_paths,
                     unpack=True)


def multi_split_test():
    return multi_base_test(os.path.split, faster_os.path.multi_split, paths)


def multi_splitdrive_test():
    return multi_base_test(os.path.splitdrive, faster_os.path.multi_splitdrive,
                           paths)


def multi_commonpath_test():
    return multi_base_test(os.path.commonpath, faster_os.path.multi_commonpath,
                           valid_list_paths)


def multi_commonprefix_test():
    return multi_base_test(os.path.commonprefix,
                           faster_os.path.multi_commonprefix, list_paths)


def multi_normcase_test():
    return multi_base_test(os.path.normcase, faster_os.path.multi_normcase,
                           paths)


def multi_abspath_test():
    return multi_base_test(os.path.abspath, faster_os.path.multi_abspath,
                           paths)


def multi_normpath_test():
    return multi_base_test(os.path.normpath, faster_os.path.multi_normpath,
                           norm_paths)


def multi_basename_test():
    return multi_base_test(os.path.basename, faster_os.path.multi_basename,
                           paths)


def multi_ismount_test():
    return multi_base_test(os.path.ismount, faster_os.path.multi_ismount,
                           paths)


def multi_dirname_test():
    return multi_base_test(os.path.dirname, faster_os.path.multi_dirname,
                           paths)


def multi_expanduser_test():
    return multi_base_test(os.path.expanduser, faster_os.path.multi_expanduser,
                           paths)


def multi_relpath_test():
    return multi_base_test(os.path.relpath,
                           faster_os.path.multi_relpath,
                           rel_paths,
                           unpack=True)


def multi_isabs_test():
    return multi_base_test(os.path.isabs, faster_os.path.multi_isabs, paths)


def multi_splitext_test():
    return multi_base_test(os.path.splitext, faster_os.path.multi_splitext,
                           paths)


def multi_join_test():
    return multi_base_test(os.path.join,
                           faster_os.path.multi_join,
                           join_paths,
                           unpack=True)


def multi_base_test(os_func, faster_os_func, paths, unpack=False):
    try:
        if unpack:
            os_func_result = [os_func(*i) for i in paths]
        else:
            os_func_result = [os_func(i) for i in paths]
    except:
        print('OS crashed', paths, traceback.format_exc())

    faster_os_func_result = faster_os_func(paths)

    if os_func_result != faster_os_func_result:
        print(f'\n\nEquality "{paths}":')
        print(f'       os_func: {os_func_result}')
        print(f'faster_os_func: {faster_os_func_result}')

        if type(faster_os_func_result) != type(os_func_result):
            print(f'\ntype: {type(os_func_result)}')
            print(f'type: {type(faster_os_func_result)}\n\n')

        print(f'Failed test.')
        return False

    print('Successfully passed this test.')
    return True


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
    # ('split', split_test),
    # ('splitdrive', splitdrive_test),
    # ('ismount', ismount_test),
    # ('normpath', normpath_test),
    # ('abspath', abspath_test),
    # ('expanduser', expanduser_test),
    # ('relpath', relpath_test),
    # ('normcase', normcase_test),
    # ('isabs', isabs_test),
    # ('join', join_test),
    # ('basename', basename_test),
    # ('dirname', dirname_test),
    # ('commonpath', commonpath_test),
    # ('commonprefix', commonprefix_test),
    # ('splitext', splitext_test),
    ('multi_split_test', multi_split_test),
    ('multi_splitdrive_test', multi_splitdrive_test),
    ('multi_commonpath_test', multi_commonpath_test),
    ('multi_commonprefix_test', multi_commonprefix_test),
    ('multi_normcase_test', multi_normcase_test),
    ('multi_abspath_test', multi_abspath_test),
    ('multi_normpath_test', multi_normpath_test),
    ('multi_basename_test', multi_basename_test),
    ('multi_ismount_test', multi_ismount_test),
    ('multi_dirname_test', multi_dirname_test),
    ('multi_expanduser_test', multi_expanduser_test),
    ('multi_relpath_test', multi_relpath_test),
    ('multi_isabs_test', multi_isabs_test),
    ('multi_splitext_test', multi_splitext_test),
    ('multi_join_test', multi_join_test),
]
