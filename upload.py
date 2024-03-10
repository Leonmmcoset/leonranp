#To upload,run this python file.
from os import *
print('---Start Upload---')
system(f'del /Q build')
system(f'del /Q dist')
system(f'del /Q leonranp.egg-info')
system(f'python3 setup.py sdist bdist_wheel')
system(f'python3 -m twine upload dist/*')
print('---End Upload---')