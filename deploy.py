import shutil
import os

username = '__token__'
password = 'pypi-340cec51-4737-4cde-a579-0b5bb3cbb686'

username = 'abtco'
password = 'M_K6Yf*jvcF.79n'

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

# os.system('py -m twine upload --repository pypi dist/*')

print(
    f'py -m twine upload --repository testpypi dist/* --verbose -u "{username}" -p "{password}"'
)
os.system(
    f"py -m twine upload -u {username} -p {password} --repository testpypi dist/* --verbose"
)
