from setuptools import setup, find_packages
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

ext_modules = cythonize(
    pyx_paths,
    compiler_directives={
        'language_level': "3",
    },
)

with open("README.md", encoding='utf8') as file:
    long_description = file.read()

setup(name="faster-os",
      version="0.0.1",
      packages=find_packages(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.8",
      ],
      license="MIT",
      author="American Best Technologies Company",
      description="Up to 6700% faster OS module.",
      long_description=long_description,
      long_description_content_type='text/markdown',
      url="https://github.com/American-Best-Technologies-Company/faster-os",
      ext_modules=ext_modules,
      install_requires=['Cython>=3.0.0a9'])