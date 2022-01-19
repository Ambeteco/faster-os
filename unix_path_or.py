import pwd


def normpath(path):
    return path



try:
    from posix import _path_normpath

except ImportError:
    def normpath(path):        
        sep = '/'
        empty = ''
        dot = '.'
        dotdot = '..'

        if not path:
            return '.'

        initial_slashes = path.startswith('/')

        if (initial_slashes and
            path.startswith(sep*2) and not path.startswith(sep*3)):
            initial_slashes = 2

        comps = path.split(sep)
        new_comps = []

        for comp in comps:
            if comp in (empty, dot):
                continue
            if (comp != dotdot or (not initial_slashes and not new_comps) or
                 (new_comps and new_comps[-1] == dotdot)):
                new_comps.append(comp)
            elif new_comps:
                new_comps.pop()

        comps = new_comps
        path = sep.join(comps)
        if initial_slashes:
            path = sep*initial_slashes + path

        return path or dot

else:
    def normpath(path):
        return _path_normpath(path) or "."


def abspath(path):
    if not isabs(path):
        cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


def isabs(path):
    return path.startswith('/')

import os


def normcase(path):
    return path


def split(path):
    last_slash = path.rfind('/')

    if last_slash == -1:
        return '', path

    if last_slash == 0:
        return '/', path[1:]

    base = path[:last_slash]
    tail = path[last_slash + 1:]

    return base, tail


def splitdrive(path):
    return '', path

def isabs(path):
    path = splitdrive(path)[1]
    return bool(path) and path[0] == '/'


def join(path, *paths):
    joined = '/'.join(paths)
    if not path:
        return joined    	

    path = path.rstrip('/')
    return f"{path}/{joined}"


def splitext(path):
    ext_ind = path.rfind('.')
    ext = path[ext_ind:]

    if ext_ind == -1 or '/' in ext:
        return (path, '')

    return (path[:ext_ind], ext)


def basename(path):
    return split(path)[1]


def dirname(path):
    return split(path)[0]


def ismount(path):
    return path == '/'


def expanduser(path):    
    if path.startswith('~/'):
        home = [
            os.environ.get('HOMEPATH'),
            os.environ.get('HOME'),
        ]

        try:
            home = list(filter(bool, home))[0]
        except:
            home = f'/home/{os.environ.get("USERNAME")}'

        return f'{home}/{path[2:]}'

    if path.startswith('~'):
        sep_loc = path.find('/')
        username = path[1:None if sep_loc == -1 else sep_loc]     

        try:
            user_path = pwd.getpwnam(username).pw_dir
            return f'{user_path}{path[len(username) + 1:]}'
        except:
            return path

    return path




def relpath(tail, root=None):
    if root is None:
        root = os.getcwd()

    if not root:
        return f'{"/.." * (tail.count("/") + 1)}{tail}'[1:]

    if tail.startswith(root):
        return tail[len(root) + 1:]

    for i, chars in enumerate(zip(tail, root)):
        tail_char, root_char = chars
        if tail_char != root_char:
            break

    dots = "../" * (root.count('/') - tail[:i].count('/') + 1)
    return f'{dots}{tail[i:]}'


def commonprefix(paths, lower=False):
    if lower:
        paths = [path.lower() for path in paths]

    min_path = min(paths)
    max_path = max(paths)

    for i, char in enumerate(min_path):
        if char != max_path[i]:
            return min_path[:i]

    return min_path


def commonpath(paths, lower=False):
    if lower:
        paths = [path.lower() for path in paths]

    splitted = [path.split('/') for path in paths]

    min_splitted = min(splitted)
    max_splitted = max(splitted)

    for index, (path, path2) in enumerate(zip(min_splitted, max_splitted)):
        if path != path2:
            if min_splitted[:index] == ['']:
                return '/'

            result = '/'.join(min_splitted[:index])
            return result

    return '/'.join(min_splitted)
