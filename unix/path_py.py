import cython
import pwd
import os

try:
    from posix import _path_normpath
except ImportError:

    def normpath(path: str) -> str:
        sep: str = '/'
        empty: str = ''
        dot: str = '.'
        dotdot: str = '..'

        if not path:
            return '.'

        initial_slashes: cython.bint = path.startswith('/')

        if (initial_slashes and path.startswith(sep * 2)
                and not path.startswith(sep * 3)):
            initial_slashes = 2

        comps: list = path.split(sep)
        new_comps: list = []

        for comp in comps:
            if comp in (empty, dot):
                continue
            if (comp != dotdot or (not initial_slashes and not new_comps)
                    or (new_comps and new_comps[-1] == dotdot)):
                new_comps.append(comp)
            elif new_comps:
                new_comps.pop()

        comps = new_comps
        path = sep.join(comps)
        if initial_slashes:
            path = sep * initial_slashes + path

        return path or dot

else:

    def normpath(path: str) -> str:
        return _path_normpath(path) or "."


@cython.exceptval(check=False)
@cython.ccall
def abspath(path: str) -> str:
    if not isabs(path):
        cwd: str = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


@cython.exceptval(check=False)
@cython.ccall
def isabs(path: str) -> cython.bint:
    return path.startswith('/')


@cython.exceptval(check=False)
@cython.ccall
def normcase(path: str) -> str:
    return path


@cython.exceptval(check=False)
@cython.ccall
def split(path: str) -> tuple:
    last_slash: cython.int = path.rfind('/')

    if last_slash == -1:
        return '', path

    if last_slash == 0:
        return '/', path[1:]

    base: str = path[:last_slash]
    tail: str = path[last_slash + 1:]

    return base, tail


@cython.exceptval(check=False)
@cython.ccall
def splitdrive(path: str) -> tuple:
    return '', path


def join(path: str, *paths: list) -> str:
    joined: str = '/'.join(paths)
    if not path:
        return joined

    path = path.rstrip('/')
    return f"{path}/{joined}"


@cython.exceptval(check=False)
@cython.ccall
def splitext(path: str) -> tuple:
    ext_ind: cython.int = path.rfind('.')
    ext: str = path[ext_ind:]

    if ext_ind == -1 or '/' in ext:
        return (path, '')

    return (path[:ext_ind], ext)


@cython.exceptval(check=False)
@cython.ccall
def basename(path: str) -> str:
    return split(path)[1]


@cython.exceptval(check=False)
@cython.ccall
def dirname(path: str) -> str:
    return split(path)[0]


@cython.exceptval(check=False)
@cython.ccall
def ismount(path: str) -> cython.bint:
    return path == '/'


@cython.exceptval(check=False)
@cython.ccall
def expanduser(path: str) -> str:
    if path.startswith('~/'):
        home: list = [
            os.environ.get('HOMEPATH'),
            os.environ.get('HOME'),
        ]

        try:
            home: str = list(filter(bool, home))[0]
        except:
            home: str = f'/home/{os.environ.get("USERNAME")}'

        return f'{home}/{path[2:]}'

    if path.startswith('~'):
        sep_loc: cython.int = path.find('/')
        username: str = path[1:None if sep_loc == -1 else sep_loc]

        try:
            user_path: str = pwd.getpwnam(username).pw_dir
            return f'{user_path}{path[len(username) + 1:]}'
        except:
            return path

    return path


@cython.exceptval(check=False)
@cython.ccall
def relpath(tail: str, root=None) -> str:
    if root is None:
        root: str = os.getcwd()

    if not root:
        return f'{"/.." * (tail.count("/") + 1)}{tail}'[1:]

    if tail.startswith(root):
        return tail[len(root) + 1:]

    for i, chars in enumerate(zip(tail, root)):
        tail_char, root_char = chars
        if tail_char != root_char:
            break

    dots: str = "../" * (root.count('/') - tail[:i].count('/') + 1)
    return f'{dots}{tail[i:]}'


@cython.exceptval(check=False)
@cython.ccall
def commonprefix(paths: list) -> str:
    min_path: str = min(paths)
    max_path: str = max(paths)

    for i, char in enumerate(min_path):
        if char != max_path[i]:
            return min_path[:i]

    return min_path


@cython.exceptval(check=False)
@cython.ccall
def commonpath(paths, lower=False) -> str:
    if lower:
        paths: list = [path.lower() for path in paths]

    splitted: list = [path.split('/') for path in paths]

    min_splitted: list = min(splitted)
    max_splitted: list = max(splitted)

    for index, (path, path2) in enumerate(zip(min_splitted, max_splitted)):
        if path != path2:
            if min_splitted[:index] == ['']:
                return '/'

            result: str = '/'.join(min_splitted[:index])
            return result

    return '/'.join(min_splitted)


@cython.exceptval(check=False)
@cython.ccall
def multi_split(paths: list) -> list:
    return [split(path) for path in paths]
