color f
py setup.py build_ext --inplace
if %errorlevel% neq 0 pause
del unix\*.c /q
del win\*.c /q
rd /s /q build
exit