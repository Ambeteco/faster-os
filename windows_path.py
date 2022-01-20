import cython
import os


@cython.exceptval(check=False)
@cython.ccall
def normpath(path: cython.str) -> cython.str:
    special_prefixes: cython.tuple = ('\\\\.\\', '\\\\?\\')

    if path.startswith(special_prefixes):
        return path

    prefix: cython.str

    path = path.replace('/', '\\')
    prefix, path = splitdrive(path)

    if path.startswith('\\'):
        prefix: cython.str = f'{prefix}\\'
        path: cython.str = path.lstrip('\\')

    comps: cython.list = path.split('\\')
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


@cython.exceptval(check=False)
@cython.ccall
def _abspath_fallback(path: cython.str) -> cython.str:
    if not isabs(path):
        cwd: cython.str = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


@cython.exceptval(check=False)
@cython.ccall
def normcase(path: cython.str) -> cython.str:
    path = path.replace('/', '\\')
    path = path.lower()
    return path


@cython.exceptval(check=False)
@cython.ccall
def split(path: cython.str) -> cython.tuple:
    last_slash: cython.int = path.rfind('\\')

    if last_slash == -1:
        if ':' in path:
            return path[:2], path[2:]
        return '', path

    base: cython.str = path[:last_slash]
    tail: cython.str = path[last_slash + 1:]

    if base[-1] == ':':
        base = f'{base}\\'

    return base, tail


@cython.exceptval(check=False)
@cython.cfunc
def csplit(path: cython.str) -> cython.tuple:
    last_slash: cython.int = path.rfind('\\')

    if last_slash == -1:
        return path[:2], path[2:]

    base: cython.str = path[:last_slash]
    tail: cython.str = path[last_slash + 1:]

    if base[-1] == ':':
        base = f'{base}\\'

    return base, tail


@cython.exceptval(check=False)
@cython.ccall
def splitdrive(path: cython.str) -> cython.tuple:
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


@cython.exceptval(check=False)
@cython.ccall
def isabs(path: cython.str) -> cython.bint:
    if path.startswith('\\\\?\\'):
        return True

    path = splitdrive(path)[1]
    return not not path and path[0] == '\\'


def join(path: cython.str, *paths) -> cython.str:
    joined: cython.str = '\\'.join(paths)
    path = path.rstrip('\\')

    if path[-1] == ':':
        return f"{path}{joined}"
    return f"{path}\\{joined}"


@cython.exceptval(check=False)
@cython.ccall
def splitext(path: cython.str) -> cython.tuple:
    ext_ind: cython.int = path.rfind('.')
    ext: cython.str = path[ext_ind:]

    if ext_ind == -1 or '\\' in ext:
        return (path, '')

    return path[:ext_ind], ext


@cython.exceptval(check=False)
@cython.ccall
def basename(path: cython.str) -> cython.str:
    return split(path)[1]


@cython.exceptval(check=False)
@cython.ccall
def dirname(path: cython.str) -> cython.str:
    return split(path)[0]


@cython.exceptval(check=False)
@cython.ccall
def ismount(path: cython.str) -> cython.bint:
    rest: cython.str
    root: cython.str

    path = abspath(path)

    return len(path) == 2 and path[1] == ':'
    return root and not rest.strip('\\')


@cython.exceptval(check=False)
@cython.ccall
def expanduser(path: cython.str) -> cython.str:
    if path.startswith('~\\'):
        userprofile: cython.str = os.environ.get('USERPROFILE', '')
        return f'{userprofile}\\{path[2:]}'

    if path.startswith('~'):
        sep_loc: cython.int = path.find('\\')
        username: cython.str = path[1:None if sep_loc == -1 else sep_loc]
        userprofile = os.environ.get('USERPROFILE', '')

        if os.environ.get('USERNAME') != username:
            home: cython.str = split(userprofile)[0]
            return f'{home}\\{path[1:]}'

        return f'{userprofile}\\{path[1:]}'

    return path


@cython.exceptval(check=False)
@cython.ccall
def relpath(tail: cython.str, root=None) -> cython.str:
    if root is None:
        root: cython.str = os.getcwd()

    if tail.startswith(root):
        return tail[len(root) + 1:]

    i: cython.int
    chars: cython.tuple
    tail_char: cython.str
    root_char: cython.str

    for i, chars in enumerate(zip(tail, root)):
        tail_char, root_char = chars
        if tail_char != root_char:
            break

    dots: cython.str = "..\\" * (root.count('\\') - tail[:i].count('\\') + 1)
    return f'{dots}{tail[i:]}'


@cython.exceptval(check=False)
@cython.ccall
def commonprefix(paths) -> cython.str:
    min_path: cython.str = min(paths)
    max_path: cython.str = max(paths)

    i: cython.int = 0
    char: cython.str

    for char in min_path:
        if char != max_path[i]:
            return min_path[:i]
        i += 1

    return min_path


@cython.exceptval(check=False)
@cython.ccall
def commonpath(paths) -> cython.str:
    splitted: cython.list = [path.split('\\') for path in paths]

    min_splitted: cython.list = min(splitted)
    max_splitted: cython.list = max(splitted)

    index: cython.int
    path: cython.str
    path2: cython.str
    result: cython.str

    for index, (path, path2) in enumerate(zip(min_splitted, max_splitted)):
        if path != path2:
            result = '\\'.join(min_splitted[:index])

            if result[-1] == ':':
                return result + '\\'
            return result

    return '\\'.join(min_splitted)


@cython.exceptval(check=False)
@cython.ccall
def multi_split(paths) -> cython.list:
    return [split(path) for path in paths]


try:
    from nt import _getfullpathname

    def abspath(path: cython.str) -> cython.str:
        try:
            return _getfullpathname(normpath(path))
        except:
            return _abspath_fallback(path)

except ImportError:
    abspath = _abspath_fallback
