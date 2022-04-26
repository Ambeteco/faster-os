# Faster OS - up to 6800% faster OS replacement!

Faster OS is a drop-in replacement for Python's standard 'OS' module. Faster OS offers **32** fully-rewritten, optimized, and speeded-up functions, that replace ones in the `os.path` module. 

Thanks to Faster OS, you can process **1,400,000 paths in just a minute**, while it would take **more than an hour with an OS module.**

```python
# Use Faster OS to save hours of processing time!
# The only thing you need to do is write...
import faster_os as os
```

##### Save your time - use Faster OS to process millions of paths in *seconds*.



At ABTco, we use Faster OS in our own projects:

- **MyQuickMac Neo** - A revolutionary program for AI-powered care of your Mac - www.myquickmac.com

- **MyQuickMac Lite** - An innovative program for AI file management - www.myquickmac.com/lite

- **4-Organizer** - A powerful program to automatically unclutter your Windows PC, powered by AI - [[www.4organizer.com](http://www.4organizer.com)]()

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

| Function     | Paths amount | Times Faster | Faster OS time      | OS time             |
| ------------ | ------------ | ------------ | ------------------- | ------------------- |
| split        | 5500         | 1105%        | 0.8109837           | 0.07337720000000003 |
| splitdrive   | 5500         | 445%         | 0.3849445           | 0.08641769999999993 |
| normcase     | 5500         | 313%         | 0.16082829999999992 | 0.05131709999999989 |
| splitext     | 5500         | 938%         | 0.5017187000000003  | 0.05350240000000017 |
| join         | 5000         | 1442%        | 1.4388798           | 0.09976049999999992 |
| relpath      | 5500         | 3653%        | 12.1418572          | 0.3323682000000012  |
| ismount      | 5500         | 3620%        | 71.5931377          | 1.977675199999993   |
| normpath     | 6500         | 326%         | 1.962145300000003   | 0.6026786000000044  |
| expanduser   | 5500         | 493%         | 0.15395150000000513 | 0.03124459999999374 |
| abspath      | 5500         | 180%         | 3.5075001000000015  | 1.9471451000000002  |
| isabs        | 5500         | 760%         | 0.6911477000000019  | 0.0909885000000088  |
| basename     | 5500         | 1217%        | 0.8403222000000028  | 0.0690242000000012  |
| dirname      | 5500         | 1236%        | 0.8473003000000006  | 0.0685450000000003  |
| commonpath   | 5000         | 738%         | 4.429664799999998   | 0.599851000000001   |
| commonprefix | 5000         | 356%         | 0.9480839999999944  | 0.26616070000000036 |

Multi-functions benchmark results:

| Function           | Chunks amount (each 50-100 paths) | Times Faster | Faster OS time       | OS time             |
| ------------------ | --------------------------------- | ------------ | -------------------- | ------------------- |
| multi_commonpath   | 1000                              | 761%         | 0.11673199999999995  | 0.8886366           |
| multi_commonprefix | 1000                              | 435%         | 0.04917400000000005  | 0.2137264000000001  |
| multi_abspath      | 4500                              | 195%         | 1.3105861000000005   | 2.5564814           |
| multi_ismount      | 4500                              | 6853%        | 1.2878387999999887   | 88.25886229999999   |
| multi_expanduser   | 4500                              | 448%         | 0.06808089999999822  | 0.30506679999999164 |
| multi_relpath      | 1100                              | 3772%        | 0.06462209999999402  | 2.4374396000000047  |
| multi_split        | 4500                              | 1475%        | 0.04426279999999849  | 0.6528628000000083  |
| multi_splitdrive   | 4500                              | 628%         | 0.04761290000000429  | 0.29895400000000905 |
| multi_normcase     | 4500                              | 451%         | 0.029892300000000205 | 0.1348015000000089  |
| multi_normpath     | 1300                              | 362%         | 0.11940829999998925  | 0.432430399999987   |
| multi_basename     | 4500                              | 1599%        | 0.04234699999999236  | 0.6770831000000044  |
| multi_dirname      | 4500                              | 1644%        | 0.04189519999999902  | 0.6888534999999933  |
| multi_isabs        | 4500                              | 1023%        | 0.05393420000000049  | 0.5514948000000004  |
| multi_splitext     | 4500                              | 1282%        | 0.03180009999999811  | 0.4077908000000008  |
| multi_join         | 1000                              | 1418%        | 0.02047290000000146  | 0.29022019999999316 |

We recommend using `multi` functions <u>when the list has more than 250 elements.</u> For smaller lists, using `multi `functions is ineffective.



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

## Platforms

- ✅ Windows
- ✅ Linux/UNIX
- ✅ macOS
- ✅ Android, Raspberry Pi, BSD, *NIX

## Requisites

- Python 3
- 64-bit
- C build tools:
  - For Windows: Have Visual Studio installed
  
  - For UNIX: GCC (probably already installed)
  
  - For macOS: Have XCode CMD tools installed

## License

Faster OS is licensed under Mozilla Public License 2.0. It means that you can use it in commercial/proprietary projects, with closed source code. You **don't need to disclose the source code.**


