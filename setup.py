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

setup(
    name="faster-os",
    version="0.0.2",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: MIT License",
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
    license="MIT",
    author_email='contact@abtco.us',
    author="American Best Technologies Company",
    description="Up to 6700% faster OS module.",
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
    install_requires=['Cython>=3.0.0a9'],
)
