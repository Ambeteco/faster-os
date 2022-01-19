from os import *
import platform

if platform.system() == 'Windows':
    from windows_path import *
elif platform.system() == 'Darwin':
    from unix_path import *
else:
    from unix_path import *
