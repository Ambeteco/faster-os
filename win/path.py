from os.path import *
import cython
import os


# @cython.exceptval(check=False)
@cython.ccall
def normpath(path: str) -> str:
    special_prefixes: tuple = ('\\\\.\\', '\\\\?\\')

    if path.startswith(special_prefixes):
        return path

    prefix: str

    path = path.replace('/', '\\')
    prefix, path = splitdrive(path)

    if path.startswith('\\'):
        prefix: str = f'{prefix}\\'
        path: str = path.lstrip('\\')

    comps: list = path.split('\\')
    i: cython.int = 0

    while i < len(comps):
        if not comps[i] or comps[i] == '.':
            del comps[i]

        elif comps[i] == '..':
            if i > 0 and comps[i - 1] != '..':
                del comps[i - 1:i + 1]
                i -= 1
            elif i == 0 and prefix.endswith('\\'):
                del comps[i]
            else:
                i += 1

        else:
            i += 1

    if not prefix and not comps:
        comps.append('.')

    return prefix + '\\'.join(comps)


# @cython.exceptval(check=False)
@cython.ccall
def _abspath_fallback(path: str) -> str:
    if not isabs(path):
        cwd: str = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


# @cython.exceptval(check=False)
@cython.ccall
def normcase(path: str) -> str:
    path = path.replace('/', '\\')
    path = path.lower()
    return path


# @cython.exceptval(check=False)
@cython.ccall
def split(path: str) -> tuple:
    last_slash: cython.int = path.rfind('\\')

    if last_slash == -1:
        if ':' in path:
            return path[:2], path[2:]
        return '', path

    base: str = path[:last_slash]
    tail: str = path[last_slash + 1:]

    if base[-1] == ':':
        base = f'{base}\\'

    return base, tail


# @cython.exceptval(check=False)
@cython.ccall
def splitdrive(path: str) -> tuple:
    colon_loc: cython.int = path.find(':')

    if colon_loc == -1:
        unc_base_ind: cython.int = path.find('\\', 2)

        if not path or path[0] != '\\':
            return '', path

        unc_path_ind: cython.int = path.find('\\', unc_base_ind + 1)
        result = path[:unc_path_ind], path[unc_path_ind:]
        return result

    result = path[:colon_loc + 1], path[colon_loc + 1:]
    return result


# @cython.exceptval(check=False)
@cython.ccall
def isabs(path: str) -> cython.bint:
    if path.startswith('\\\\?\\'):
        return True

    path = splitdrive(path)[1]
    return path and path[0] == '\\'


def join(path: str, *paths) -> str:
    joined: str = '\\'.join(paths)
    path = path.rstrip('\\')

    if path[-1] == ':':
        return f"{path}{joined}"
    return f"{path}\\{joined}"


# @cython.exceptval(check=False)
@cython.ccall
def splitext(path: str) -> tuple:
    ext_ind: cython.int = path.rfind('.')
    ext: str = path[ext_ind:]

    if ext_ind == -1 or '\\' in ext:
        return (path, '')

    return path[:ext_ind], ext


# @cython.exceptval(check=False)
@cython.ccall
def basename(path: str) -> str:
    return split(path)[1]


# @cython.exceptval(check=False)
@cython.ccall
def dirname(path: str) -> str:
    return split(path)[0]


# @cython.exceptval(check=False)
@cython.ccall
def ismount(path: str) -> cython.bint:
    rest: str
    root: str

    path = abspath(path)

    return len(path) == 2 and path[1] == ':'


# @cython.exceptval(check=False)
@cython.ccall
def expanduser(path: str) -> str:
    if path.startswith('~\\'):
        userprofile: str = os.environ.get('USERPROFILE', '')
        return f'{userprofile}\\{path[2:]}'

    if path.startswith('~'):
        sep_loc: cython.int = path.find('\\')
        username: str = path[1:None if sep_loc == -1 else sep_loc]
        userprofile = os.environ.get('USERPROFILE', '')

        if os.environ.get('USERNAME') != username:
            home: str = split(userprofile)[0]
            return f'{home}\\{path[1:]}'

        return f'{userprofile}\\{path[1:]}'

    return path


# @cython.exceptval(check=False)
@cython.ccall
def relpath(tail: str, root=None) -> str:
    if root is None:
        root: str = os.getcwd()

    if tail.startswith(root):
        return tail[len(root) + 1:]

    i: cython.int
    chars: tuple
    tail_char: str
    root_char: str

    for i, chars in enumerate(zip(tail, root)):
        tail_char, root_char = chars
        if tail_char != root_char:
            break

    dots: str = "..\\" * (root.count('\\') - tail[:i].count('\\') + 1)
    return f'{dots}{tail[i:]}'


# @cython.exceptval(check=False)
@cython.ccall
def commonprefix(paths) -> str:
    min_path: str = min(paths)
    max_path: str = max(paths)

    i: cython.int = 0
    char: str

    for char in min_path:
        if char != max_path[i]:
            return min_path[:i]
        i += 1

    return min_path


# @cython.exceptval(check=False)
@cython.ccall
def commonpath(paths) -> str:
    splitted: list = [path.split('\\') for path in paths]

    min_splitted: list = min(splitted)
    max_splitted: list = max(splitted)

    index: cython.int
    path: str
    path2: str
    result: str

    for index, (path, path2) in enumerate(zip(min_splitted, max_splitted)):
        if path != path2:
            result = '\\'.join(min_splitted[:index])

            if result[-1] == ':':
                return result + '\\'
            return result

    return '\\'.join(min_splitted)


try:
    from nt import _getfullpathname

    def abspath(path: str) -> str:
        try:
            return _getfullpathname(normpath(path))
        except:
            return _abspath_fallback(path)

except ImportError:
    abspath = _abspath_fallback


# @cython.exceptval(check=False)
@cython.ccall
def multi_split(paths) -> list:
    return [split(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_normpath(paths) -> list:
    return [normpath(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_normcase(paths) -> list:
    return [normcase(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_splitdrive(paths) -> list:
    return [splitdrive(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_isabs(paths) -> list:
    return [isabs(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_join(paths) -> list:
    results: list = []

    for path in paths:
        results.append(join(*path))
    
    return results
    # return [join(*path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_splitext(paths) -> list:
    return [splitext(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_basename(paths) -> list:
    return [basename(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_dirname(paths) -> list:
    return [dirname(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_relpath(paths) -> list:
    return [relpath(*path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_expanduser(paths) -> list:
    return [expanduser(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_ismount(paths) -> list:
    return [ismount(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_abspath(paths) -> list:
    return [abspath(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_commonprefix(paths) -> list:
    return [commonprefix(path) for path in paths]


# @cython.exceptval(check=False)
@cython.ccall
def multi_commonpath(paths) -> list:
    return [commonpath(path) for path in paths]
