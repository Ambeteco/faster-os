from setuptools import setup, Extension
import platform

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

file_ext = 'py' if USE_CYTHON else 'c'
platform_folder = 'win' if platform.system() == 'Windows' else 'unix'

ext_modules = [
    Extension("faster_os", [f"faster_os.{file_ext}"]),
    Extension("faster_os.path", [f"{platform_folder}/path.{file_ext}"]),
    Extension("faster_os.generic", [f'{platform_folder}/generic.{file_ext}']),
]

if USE_CYTHON:
    ext_modules = cythonize(
        ext_modules,
        compiler_directives={
            'language_level': "3",
        },
    )

with open("README.md", encoding='utf8') as file:
    long_description = file.read()

setup(
    name="faster-os",
    version="0.0.11",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        'Intended Audience :: Developers',
        'Programming Language :: Cython',
        'Topic :: Office/Business',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Operating System',
        'Topic :: Utilities',
    ],
    license="MPL 2.0",
    author_email='contact@abtco.us',
    author="American Best Technologies Company",
    description="Up to 6700% faster OS module.",
    packages=['unix', 'win'],
    package_dir={'faster_os': 'faster_os'},
    long_description=long_description,
    project_urls={
        "Bug Tracker":
        "https://github.com/American-Best-Technologies-Company/faster-os/issues",
        "Our website": 'http://www.abtco.us',
        "Used by MyQuickMac": 'http://www.myquickmac.com',
    },
    long_description_content_type='text/markdown',
    url="https://github.com/American-Best-Technologies-Company/faster-os",
    ext_modules=ext_modules,
    install_requires=[],
)
"""
faster-than
os
optimized
speedup
speededup
faster
path
file
directory
paths manipulations
files processing
data processing
"""
