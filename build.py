import shutil
import os

os.system("color f")
os.system('py cysetup.py build_ext && if %errorlevel% neq 0 pause')

release_name = [i for i in os.listdir('build') if 'lib' in i][0]
release = os.path.join(os.getcwd(), 'build', release_name, 'FasterOS')
print(release, os.getcwd())
shutil.copytree(release, os.getcwd(), dirs_exist_ok=True)

os.system('del unix\\*.c /q')
os.system('del win\\*.c /q')
os.system('rd /s /q build')
