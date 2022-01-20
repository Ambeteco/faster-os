py setup.py build_ext --inplace
if %errorlevel% neq 0 pause
del *.c /q
exit