from os import *
import platform

if platform.system() == 'Windows':
    from win.path import *
elif platform.system() == 'Darwin':
    from unix.path import *
else:
    from unix.path import *
