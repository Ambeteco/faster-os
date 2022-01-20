import os


def normpath(path):
    special_prefixes = ('\\\\.\\', '\\\\?\\')

    if path.startswith(special_prefixes):
        return path

    path = path.replace('/', '\\')
    prefix, path = splitdrive(path)

    if path.startswith('\\'):
        prefix = f'{prefix}\\'
        path = path.lstrip('\\')

    comps = path.split('\\')
    i = 0

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


def _abspath_fallback(path):
    if not isabs(path):
        cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


def normcase(path):
    path = path.replace('/', '\\')
    path = path.lower()
    return path


def split(path):
    last_slash = path.rfind('\\')

    if last_slash == -1:
        if ':' in path:
            return path[:2], path[2:]
        return '', path

    base = path[:last_slash]
    tail = path[last_slash + 1:]

    if base[-1] == ':':
        base = f'{base}\\'

    return base, tail


def csplit(path):
    last_slash = path.rfind('\\')

    if last_slash == -1:
        return path[:2], path[2:]

    base = path[:last_slash]
    tail = path[last_slash + 1:]

    if base[-1] == ':':
        base = f'{base}\\'

    return base, tail


def splitdrive(path):
    colon_loc = path.find(':')

    if colon_loc == -1:
        unc_base_ind = path.find('\\', 2)

        if not path or path[0] != '\\':
            return '', path

        unc_path_ind = path.find('\\', unc_base_ind + 1)
        result = path[:unc_path_ind], path[unc_path_ind:]
        return result

    result = path[:colon_loc + 1], path[colon_loc + 1:]
    return result


def isabs(path):
    if path.startswith('\\\\?\\'):
        return True

    path = splitdrive(path)[1]
    return not not path and path[0] == '\\'


def join(path, *paths):
    joined = '\\'.join(paths)
    path = path.rstrip('\\')

    if path[-1] == ':':
        return f"{path}{joined}"
    return f"{path}\\{joined}"


def splitext(path):
    ext_ind = path.rfind('.')
    ext = path[ext_ind:]

    if ext_ind == -1 or '\\' in ext:
        return (path, '')

    return path[:ext_ind], ext


def basename(path):
    return split(path)[1]


def dirname(path):
    return split(path)[0]


def ismount(path):

    path = abspath(path)

    return len(path) == 2 and path[1] == ':'
    return root and not rest.strip('\\')


def expanduser(path):
    if path.startswith('~\\'):
        userprofile = os.environ.get('USERPROFILE', '')
        return f'{userprofile}\\{path[2:]}'

    if path.startswith('~'):
        sep_loc = path.find('\\')
        username = path[1:None if sep_loc == -1 else sep_loc]
        userprofile = os.environ.get('USERPROFILE', '')

        if os.environ.get('USERNAME') != username:
            home = split(userprofile)[0]
            return f'{home}\\{path[1:]}'

        return f'{userprofile}\\{path[1:]}'

    return path


def relpath(tail, root=None):
    if root is None:
        root = os.getcwd()

    if tail.startswith(root):
        return tail[len(root) + 1:]

    for i, chars in enumerate(zip(tail, root)):
        tail_char, root_char = chars
        if tail_char != root_char:
            break

    dots = "..\\" * (root.count('\\') - tail[:i].count('\\') + 1)
    return f'{dots}{tail[i:]}'


def commonprefix(paths):
    min_path = min(paths)
    max_path = max(paths)

    i = 0

    for char in min_path:
        if char != max_path[i]:
            return min_path[:i]
        i += 1

    return min_path


def commonpath(paths):
    splitted = [path.split('\\') for path in paths]

    min_splitted = min(splitted)
    max_splitted = max(splitted)

    for index, (path, path2) in enumerate(zip(min_splitted, max_splitted)):
        if path != path2:
            result = '\\'.join(min_splitted[:index])

            if result[-1] == ':':
                return result + '\\'
            return result

    return '\\'.join(min_splitted)


def multi_split(paths):
    return [split(path) for path in paths]


try:
    from nt import _getfullpathname

    def abspath(path):
        try:
            return _getfullpathname(normpath(path))
        except:
            return _abspath_fallback(path)

except ImportError:
    abspath = _abspath_fallback
