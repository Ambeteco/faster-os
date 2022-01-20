from os import *
import platform

if platform.system() == 'Windows':
    from windows_path_py import *
elif platform.system() == 'Darwin':
    from unix_path_py import *
else:
    from unix_path_py import *
