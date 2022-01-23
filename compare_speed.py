from speed_tests import py_vs_cy
from speed_tests import os_vs_faster_os

print('Comparing FasterOS[py] vs FasterOS[cy]')
py_vs_cy.run()
print('\n' * 3)

print('Comparing FasterOS[cy] vs OS')
os_vs_faster_os.run()
