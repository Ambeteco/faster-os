import cython
import os
from win.path import split


@cython.exceptval(check=False)
@cython.cfunc
def removedirs(path: str) -> cython.void:
    while path:
        try:
            os.rmdir(path)
        except OSError:
            break

        path = split(path)[0]


@cython.exceptval(check=False)
@cython.ccall
def multi_removedirs(paths: list) -> cython.void:
    [removedirs(path) for path in paths]
