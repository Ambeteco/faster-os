from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("unix_path.py",
                            compiler_directives={'language_level': "3"}))
