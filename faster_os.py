from os import *
import platform

if platform.system() == 'Windows':
    from win import path
    from win.generic import *
else:
    from unix import path
    from unix.generic import *
