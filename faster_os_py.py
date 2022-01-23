from os import *
import platform

if platform.system() == 'Windows':
    from win import path_py as path
    from win.generic import *
else:
    from unix import path_py as path
    from unix.generic import *
