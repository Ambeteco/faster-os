from os import *
import platform

if platform.system() == 'Windows':
    from win.path import *
else:
    from unix.path import *
