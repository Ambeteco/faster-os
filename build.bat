color f
py cysetup.py build_ext
if %errorlevel% neq 0 pause
del unix\*.c /q
del win\*.c /q
rd /s /q build
exit