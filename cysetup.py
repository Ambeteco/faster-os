import os
from setuptools import setup
from Cython.Build import cythonize
import platform

pyx_paths = [
    'faster_os.py',
    "win/path.py",
    "win/generic.py",
] if platform.system() == 'Windows' else [
    'faster_os.py',
    "unix/path.py",
    "unix/generic.py",
]

pyx_paths = [os.path.join(os.getcwd(), i) for i in pyx_paths]

ext_modules = cythonize(
    pyx_paths,
    compiler_directives={
        'language_level': "3",
    },
)

setup(ext_modules=ext_modules, )
