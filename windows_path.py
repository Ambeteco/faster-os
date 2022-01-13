import genericpath

try:
    from nt import _path_normpath
except ImportError:

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

else:

    def normpath(path):
        return _path_normpath(path) or "."


try:
    from nt import _getvolumepathname
except ImportError:
    _getvolumepathname = None


def _abspath_fallback(path):
    if not isabs(path):
        cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


try:
    from nt import _getfullpathname
except ImportError:
    abspath = _abspath_fallback
else:

    def abspath(path):
        try:
            return normpath(_getfullpathname(path))
        except (OSError, ValueError):
            return _abspath_fallback(path)


import os


def normcase(path):
    return path.replace('/', '\\').lower()


def split(path):
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
        return path[:unc_path_ind], path[unc_path_ind:]

    return path[:colon_loc + 1], path[colon_loc + 1:]


def isabs(path):
    if path.startswith('\\\\?\\'):
        return True

    path = splitdrive(path)[1]
    return bool(path) and path[0] == '\\'


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

    return (path[:ext_ind], ext)


def basename(path):
    return split(path)[1]


def dirname(path):
    return split(path)[0]


def ismount(path):
    path = abspath(path)
    root, rest = splitdrive(path)
    return root and not rest.strip('\\')


def expanduser(path):
    tilde = '~'

    if not path.startswith(tilde):
        return path

    i, n = 1, len(path)
    while i < n and path[i] not in ('\\', '/'):
        i += 1

    if 'USERPROFILE' in os.environ:
        userhome = os.environ['USERPROFILE']
    elif not 'HOMEPATH' in os.environ:
        return path
    else:
        try:
            drive = os.environ['HOMEDRIVE']
        except KeyError:
            drive = ''
        userhome = join(drive, os.environ['HOMEPATH'])

    if i != 1:
        target_user = path[1:i]
        if isinstance(target_user, bytes):
            target_user = os.fsdecode(target_user)
        current_user = os.environ.get('USERNAME')

        if target_user != current_user:
            if current_user != basename(userhome):
                return path
            userhome = join(dirname(userhome), target_user)

    if isinstance(path, bytes):
        userhome = os.fsencode(userhome)

    return userhome + path[i:]


def commonpath(paths, lower=False):
    if lower:
        paths = [path.lower() for path in paths]

    min_path = min(paths, key=len)

    common_path = min_path
    common_path_len = len(common_path)

    while True:
        cropped = [path[:common_path_len] for path in paths]
        if len(set(cropped)) == 1:
            return common_path

        common_path = os.path.dirname(common_path)
        common_path_len = len(common_path)

        if splitdrive(common_path)[0] == common_path:
            return


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

    min_path = min(paths)
    max_path = max(paths)

    for i, char in enumerate(min_path):
        if char != max_path[i]:
            return min_path[:i]

    return min_path
