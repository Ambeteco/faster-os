# Faster OS - up to 6800% faster OS module replacement!
[![Downloads](https://static.pepy.tech/personalized-badge/faster-os?period=total&units=international_system&left_color=black&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/faster-os)
[![DeepSource](https://deepsource.io/gh/American-Best-Technologies-Company/faster-os.svg/?label=resolved+issues&show_trend=true&token=3oNMhJxubBfnHF2qYXh5tJZ5)](https://deepsource.io/gh/American-Best-Technologies-Company/faster-os/?ref=repository-badge)

![PyPI - Downloads](https://img.shields.io/pypi/dm/faster-os?color=blue&style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/American-Best-Technologies-Company/faster-os?style=for-the-badge)

Faster OS is a drop-in replacement for Python's standard 'OS' module. Faster OS offers **32** fully-rewritten, optimized, and speeded-up functions, that replace ones in the `os.path` module. 

Thanks to Faster OS, you can process **1,400,000 paths in just a minute**, while it would take **more than an hour with an OS module.**

```python
# Use Faster OS to save hours of processing time!
# The only thing you need to do is write...
import faster_os as os
```

##### Save your time - use Faster OS to process millions of paths in *seconds*.

At ABTco, we use Faster OS in our own projects:

- **MyQuickMac Neo** - A revolutionary program for AI-powered care of your Mac - [www.myquickmac.com](https://www.myquickmac.com)

- **MyQuickMac Lite** - An innovative program for AI file management - [www.myquickmac.com/lite](https://www.myquickmac.com/lite)

- **4-Organizer** - A powerful program to automatically unclutter your Windows PC, powered by AI - [www.4organizer.com](http://www.4organizer.com)

- **Wiper AI**  - under development, available soon

**It means that Faster OS is a stable, production-ready tool.** 

In our case, just by changing `import os` to `import faster_os as os`, Faster OS brought **35-40% speed improvements** to our programs' inner processes.

---

## Benchmarks and speed

On average, a Faster OS function is **1504% faster** than an original function from the OS module. 

The most-used functions (`split`, `join`, `splitext`) are on average **1215% faster**:

| Name       | Times Faster | Faster OS: process 1,000,000 paths | OS: process 1,000,000 paths |
| ---------- | ------------ | ---------------------------------- | --------------------------- |
| `join`     | 1530%        | 14 seconds                         | 3 minutes 20 seconds        |
| `splitext` | 1059%        | 8 seconds                          | 1 minute 33 seconds         |
| `split`    | 1190%        | 18 seconds                         | 4 minutes 43 seconds        |

Full benchmark results:

| Function     | Paths amount | Times Faster | Faster OS time | OS time |
| ------------ | ------------ | ------------ | -------------- | ------- |
| split        | 5500         | 1105%        | 0.8109         | 0.0733  |
| splitdrive   | 5500         | 445%         | 0.3849         | 0.0864  |
| normcase     | 5500         | 313%         | 0.1608         | 0.0513  |
| splitext     | 5500         | 938%         | 0.5017         | 0.0535  |
| join         | 5000         | 1442%        | 1.4388         | 0.0997  |
| relpath      | 5500         | 3653%        | 12.1418        | 0.3323  |
| ismount      | 5500         | 3620%        | 71.5931        | 1.9776  |
| normpath     | 6500         | 326%         | 1.9621         | 0.6026  |
| expanduser   | 5500         | 493%         | 0.1539         | 0.0312  |
| abspath      | 5500         | 180%         | 3.5075         | 1.9471  |
| isabs        | 5500         | 760%         | 0.6911         | 0.0909  |
| basename     | 5500         | 1217%        | 0.8403         | 0.0690  |
| dirname      | 5500         | 1236%        | 0.8473         | 0.0685  |
| commonpath   | 5000         | 738%         | 4.4296         | 0.5998  |
| commonprefix | 5000         | 356%         | 0.9480         | 0.2661  |

Multi-functions benchmark results:

| Function           | Chunks amount (each 50-100 paths) | Times Faster | Faster OS time | OS time |
| ------------------ | --------------------------------- | ------------ | -------------- | ------- |
| multi_commonpath   | 1000                              | 761%         | 0.1167         | 0.8886  |
| multi_commonprefix | 1000                              | 435%         | 0.0491         | 0.2137  |
| multi_abspath      | 4500                              | 195%         | 1.3105         | 2.5564  |
| multi_ismount      | 4500                              | 6853%        | 1.2878         | 88.2588 |
| multi_expanduser   | 4500                              | 448%         | 0.0680         | 0.3050  |
| multi_relpath      | 1100                              | 3772%        | 0.0646         | 2.4374  |
| multi_split        | 4500                              | 1475%        | 0.0442         | 0.6528  |
| multi_splitdrive   | 4500                              | 628%         | 0.0476         | 0.2989  |
| multi_normcase     | 4500                              | 451%         | 0.0298         | 0.1348  |
| multi_normpath     | 1300                              | 362%         | 0.1194         | 0.4324  |
| multi_basename     | 4500                              | 1599%        | 0.0423         | 0.6770  |
| multi_dirname      | 4500                              | 1644%        | 0.0418         | 0.6888  |
| multi_isabs        | 4500                              | 1023%        | 0.0539         | 0.5514  |
| multi_splitext     | 4500                              | 1282%        | 0.0318         | 0.4077  |
| multi_join         | 1000                              | 1418%        | 0.0204         | 0.2902  |

We recommend using `multi-functions` <u>when the given iterable has more than 250 elements.</u> For smaller lists, using `multi-functions` is ineffective.

## Introduction / How to use

```python
# Faster OS - a drop-in replacement for the 'OS' module
# Up to 6800% faster!
import faster_os

# All 'OS' functions you need, and even more!
# 32 rewritten functions, optimized for speed and performance.

faster_os.path.join('/', 'some', 'path')
>>> '/some/path'
faster_os.path.split('/some/test/path')
>>> ('/some/test', 'path')

faster_os.path.join('C:\\', 'Windows\\System32', 'LogFiles')
>>> 'C:\\Windows\\System32\\LogFiles'
faster_os.path.split('C:\\Users\\User\\Desktop')
>>> ('C:\\Users\\User', 'Desktop')

# Works both for UNIX and for Windows!
# Everything works exactly the same as in 'OS':

# -- splitext --
faster_os.path.splitext('hello world\\123.ext')
>>> ('hello world\\123', '.ext')
faster_os.path.splitext('C:\\sample_photo.jpg')
>>> ('C:\\sample_photo', '.jpg')

# -- splitdrive --
faster_os.path.splitdrive('C:\\HELLO WORLD\\SOME PATH')
>>> ('C:', '\\HELLO WORLD\\SOME PATH')
faster_os.path.splitdrive('\\\\machine\\mountpoint\\directory\\etc\\')
>>> ('\\\\machine\\mountpoint', '\\directory\\etc\\')

# -- normpath --
faster_os.path.normpath('C:\\\\hello\\\\\\world\\\\\\')
>>> 'C:\\hello\\world'
faster_os.path.normpath('An invalid\\\\\\path\\\\with many slashes\\\\\\\\\\\\')
>>> 'An invalid\\path\\with many slashes'

# -- abspath --
faster_os.path.abspath('Desktop')
>>> 'D:\\Libraries\\Desktop\\Pys\\Big\\FasterOS\\Desktop'
faster_os.path.abspath('Appdata\\Local')
>>> 'D:\\Libraries\\Desktop\\Pys\\Big\\FasterOS\\Appdata\\Local'

# -- expanduser --
faster_os.path.expanduser('~\\Downloads\\file.exe')
>>> 'C:\\Users\\Dsibe\\Downloads\\file.exe'
faster_os.path.expanduser('~\\Appdata')
>>> 'C:\\Users\\Dsibe\\Appdata'

# -- normcase --
faster_os.path.normcase('C:/HELLO WORLD/SOME/PATH/')
>>> 'c:\\hello world\\some\\path\\'
faster_os.path.normcase('C:/faster-os/a-unix-path/to-windows/path')
>>> 'c:\\faster-os\\a-unix-path\\to-windows\\path'

# -- isabs --
faster_os.path.isabs('C:\\Users\\User')
>>> True
faster_os.path.isabs('~\\user')
>>> False
faster_os.path.isabs('%USERPROFILE%\\hi')
>>> False

# -- basename --
faster_os.path.basename('C:\\HELLO WORLD\\SOME PATH')
>>> 'SOME PATH'
faster_os.path.basename('C:\\faster-os')
>>> 'faster-os'

# -- dirname --
faster_os.path.dirname('C:\\HELLO WORLD\\SOME PATH')
>>> 'C:\\HELLO WORLD'
faster_os.path.dirname('C:\\faster-os')
>>> 'C:\\'

# -- commonpath --
faster_os.path.commonpath([
    'C:\\\\Common', 'C:\\\\Common\\\\', 'C:\\\\Common\\\\123', 'C:\\\\Common\\\\Common',
    'C:\\\\Common\\\\abtco\\\\faster_os'
])
>>> 'C:\\Common'

# -- commonprefix--
faster_os.path.commonprefix([
    'C:\\\\', 'C:\\\\1\\\\123/123/123\\\\123', 'C:\\\\hello world\\\\some path',
    'C:\\\\hello world\\\\some path\\\\'
])
>>> 'C:\\'

# And 21 more functions...

# Also, Faster OS also offers special 'multi-functions'.
# Use them to process extra large lists, containing hundreds of thousands of elements!
multi_abspath, multi_basename, multi_commonpath, multi_commonprefix, multi_dirname, multi_expanduser, multi_isabs, multi_ismount, multi_join, multi_normcase, multi_normpath, multi_relpath, multi_split, multi_splitdrive, multi_splitext

# For example:
faster_os.multi_join([
    ('path/to/join', 'some path'),
    ('path/to/join', 'other path'),
    ('path/to/join', 'other path 2'),
    ('path/to/join', 'other path 3'),
    ...    
])
# We recommend using multi-functions over lists with more than 250 elements.

# Even further, Faster OS re-implements removedirs and adds remove_multiple_dirs
faster_os.removedirs('C:\\This\\Path\\Will\\Be\\Deleted')
```

## Installation

##### Via PyPi:

`pip install faster_os --upgrade`

###### Or, build from the source:

1. Clone the repository: `git clone https://github.com/American-Best-Technologies-Company/faster-os.git`

2. Run `python3 setup.py build_ext`

3. Done! Verify installation: `import faster_os`

---

## Differences from the OS module

#### Exceptions and invalid paths

If the given arguments are valid then Faster OS works absolutely the same way as the OS module. It means that if you use Faster OS on any valid path, **it will work exactly like the OS module**. 

If you will pass some invalid path as an argument to Faster OS' functions, then most of the exceptions raised by it **will not match** the ones raised by the OS module. 

For example, in this case, the exceptions raised by OS and Faster OS **are the same**:

```python
import os
os.path.join('some path', None)
>>> TypeError: join() argument must be str, bytes, or os.PathLike object, not 'NoneType'

import faster_os
faster_os.path.join('some path', None)
>>> TypeError: sequence item 0: expected str instance, NoneType found
```

But sometimes, exceptions raised **can be different**:

```python
import os
os.path.normcase(None)

>>> TypeError: expected str, bytes or os.PathLike object, not NoneType

import faster_os
faster_os.path.normcase(None)
>>> AttributeError: 'NoneType' object has no attribute 'replace'
```

The main reason for this is the main goal of Faster OS: speed.

Adding type and paths validity checks will significantly slow down Faster OS. Right now, **we do not plan to add any type checks or some validation** to the Faster OS functions. Because of this, the exceptions might be not that human-readable or easy to understand.

#### Bytes support

Currently, Faster OS supports only `str`. `bytes` support will be added in the next updates. Maybe, even `os.PathLike` object will be supported in the next releases.

---

## Platforms

- ✅ Windows
- ✅ Linux/UNIX
- ✅ macOS
- ✅ Android, Raspberry Pi, BSD, *NIX

## Requisites

- Python 3

- C build tools:
  
  - For Windows: Have Visual Studio installed
  
  - For UNIX: GCC (probably already installed)
  
  - For macOS: Have XCode CMD tools installed (type `gcc` in the Terminal to check if it's installed)

## License

Faster OS is licensed under Mozilla Public License 2.0. It means that you can use it in commercial/proprietary projects, with closed source code. You **don't need to disclose the source code.**

---

## Documentation

We recommend reading the [official OS module documentation](https://docs.python.org/3/library/os.path.html), as all Faster OS functions' behavior is 'mirrored' from the OS functions. Below, you can find short documentation on all Faster OS functions.

##### normpath

`faster_os.path.normpath(path: str) -> str`

Normalizes the path: replaces '/' to '\' on Windows (or the opposite on UNIX), and does other changes related to '.' and '..'.

##### normcase

`faster_os.path.normcase(path: str) -> str`

Lowers the path (`str.lower`) and replaces '/' to '\' on Windows (or the opposite on UNIX).

##### split

`faster_os.path.split(path: str) -> tuple`

Returns a tuple with the path splitted into directory name and base name:

Example: 'some/example/path' -> ('some/example', 'path')

##### splitdrive

`faster_os.path.splitdrive(path: str) -> tuple`

Only makes sense on Windows: splits the path into the drive and the path.

Example: `'C:\\Windows' -> ('C:', '\\Windows')`

##### isabs

`faster_os.path.isabs(path: str) -> cython.bint`

Checks if a path is absolute.

Example:

`'C:\\some absolute\\path' -> True`

`'some\\relative\\path\\' -> False`

##### join

`faster_os.path.join(path: str, *paths) -> str`

Joins all the given paths using platform delimiter ('/' or '\').

Example:

`faster_os.path.('C:\\', 'some', 'path') -> 'C:\\some\\path'`

##### splitext

`faster_os.path.splitext(path: str) -> tuple`

Splits the path into the path and extension.

Example:

`'a photo.jpg' -> ('a photo', '.jpg')`

##### basename

`faster_os.path.basename(path: str) -> str`

Returns the base name of a path.

`'C:\\some absolute\\path' -> 'path'`

##### dirname

`faster_os.path.dirname(path: str) -> str`

Returns the directory name of a path.

`'C:\\some absolute\\path' -> 'C:\\some absolute\\'`

##### ismount

`faster_os.path.ismount(path: str) -> cython.bint`

Checks if a path is a mounting point.

##### expanduser

`faster_os.path.expanduser(path: str) -> str`

Expands the '~' into the user profile or home path.

Example:

```python
'~Desktop' -> 'C:\\Users\\Desktop
'~\\Desktop' -> 'C:\\Users\\User\\Desktop
  ^^ notice this slash
```

##### relpath

`faster_os.path.relpath(tail: str, root=None) -> str`

Computes the relative path of the `tail` depending on the `root`.

If `root` is None, then it's assigned to the current working directory `os.getcwd()`.

##### commonprefix

`faster_os.path.commonprefix(paths) -> str`

Finds the common prefix of given paths.

Example:

`['faster_os/abc', 'faster_os/abcde', 'faster_os/abc123'] -> 'faster_os/abc'`

##### commonpath

`faster_os.path.commonpath(paths) -> str`

Finds the common path of given paths.

Contraty to commonprefix, finds the full path.

Example:

`['faster_os/abc', 'faster_os/abcde', 'faster_os/abc123'] -> 'faster_os'`

##### abspath

`faster_os.path.abspath(path: str) -> str`

Tries to get the absolute path using the operating system's API, or falls back to joining the path with CWD.

##### multi_split

`faster_os.path.multi_split(paths) -> list`

Takes any iterable (list, tuple, etc) and applies split to each element.

Returns a list.

##### multi_normpath

`faster_os.path.multi_normpath(paths) -> list`

Takes any iterable (list, tuple, etc) and applies normpath to each element.

Returns a list.

##### multi_normcase

`faster_os.path.multi_normcase(paths) -> list`

Takes any iterable (list, tuple, etc) and applies normcase to each element.

Returns a list.

##### multi_splitdrive

`faster_os.path.multi_splitdrive(paths) -> list`

Takes any iterable (list, tuple, etc) and applies splitdrive to each element.

Returns a list.

##### multi_isabs

`faster_os.path.multi_isabs(paths) -> list`

Takes any iterable (list, tuple, etc) and applies isabs to each element.

Returns a list.

##### multi_join

`faster_os.path.multi_join(paths) -> list`

Takes any iterable (list, tuple, etc) and applies join to each element.

Returns a list.

##### multi_splitext

`faster_os.path.multi_splitext(paths) -> list`

Takes any iterable (list, tuple, etc) and applies splitext to each element.

Returns a list.

##### multi_basename

`faster_os.path.multi_basename(paths) -> list`

Takes any iterable (list, tuple, etc) and applies basename to each element.

Returns a list.

##### multi_dirname

`faster_os.path.multi_dirname(paths) -> list`

Takes any iterable (list, tuple, etc) and applies dirname to each element.

Returns a list.

##### multi_relpath

`faster_os.path.multi_relpath(paths) -> list`

Takes any iterable (list, tuple, etc) and applies relpath to each element.

Returns a list.

##### multi_expanduser

`faster_os.path.multi_expanduser(paths) -> list`

Takes any iterable (list, tuple, etc) and applies expanduser to each element.

Returns a list.

##### multi_ismount

`faster_os.path.multi_ismount(paths) -> list`

Takes any iterable (list, tuple, etc) and applies ismount to each element.

Returns a list.

##### multi_abspath

`faster_os.path.multi_abspath(paths) -> list`

Takes any iterable (list, tuple, etc) and applies abspath to each element.

Returns a list.

##### multi_commonprefix

`faster_os.path.multi_commonprefix(paths) -> list`

Takes any iterable (list, tuple, etc) and applies commonprefix to each element.

Returns a list.

##### multi_commonpath

`faster_os.path.multi_commonpath(paths) -> list`

Takes any iterable (list, tuple, etc) and applies commonpath to each element.

Returns a list.

##### removedirs

`faster_os.removedirs(path) -> None`

Deletes all the path components until the exception is raised.

`removedirs` will try to delete each directory until the error is raised, for example, a directory is not empty or there's a permission error:
For example:

```python
Given path "C:\Users\User\Desktop\many\folders\here"
Delete "C:\Users\User\Desktop\many\folders\here"
Delete "C:\Users\User\Desktop\many\folders"
Delete "C:\Users\User\Desktop\many"
Delete "C:\Users\User\Desktop\" -> ERROR - return
```

##### remove_multiple_dirs

`faster_os.remove_multiple_dirs(paths) -> None`

Takes any iterable (list, tuple, etc) and applies `removedirs` to each element.
