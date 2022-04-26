import json
import shutil
import os

with open('creds.json') as f:
    creds = json.load(f)

username = creds['fasteros-username']
password = creds['fasteros-password']

shutil.rmtree('faster_os', ignore_errors=True)

os.makedirs('faster_os/win', exist_ok=True)
os.makedirs('faster_os/unix', exist_ok=True)

shutil.copy('faster_os.py', 'faster_os/faster_os.py')
shutil.copy('setup.py', 'faster_os/setup.py')
shutil.copy('pyproject.toml', 'faster_os/pyproject.toml')
shutil.copy('README.md', 'faster_os/README.md')

shutil.copy('win/__init__.py', 'faster_os/win/')
shutil.copy('win/path.py', 'faster_os/win/')
shutil.copy('win/generic.py', 'faster_os/win/')

shutil.copy('unix/__init__.py', 'faster_os/unix/')
shutil.copy('unix/path.py', 'faster_os/unix/')
shutil.copy('unix/generic.py', 'faster_os/unix/')

os.chdir('faster_os')
os.system('py setup.py sdist bdist_wheel')

os.system(
    f"py -m twine upload -u {username} -p {password} --repository testpypi dist/* --verbose"
)

# os.system(
#     f"py -m twine upload -u {username} -p {password} --repository pypi dist/* --verbose"
# )
