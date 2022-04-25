from speed_tests import py_vs_cy
from speed_tests import os_vs_faster_os
from speed_tests import faster_os_multi_os
from speed_tests import faster_os_multi_faster_os

# print('-' * 30)
# print('Comparing FasterOS[py] vs FasterOS[cy]')
# py_vs_cy.run()

print('-' * 30)
print('Comparing FasterOS[cy] vs OS')
os_vs_faster_os.run()

print('-' * 30)
print('Comparing FasterOS[multi] vs OS[list comprehension]')
faster_os_multi_os.run()

# print('-' * 30)
# print('Comparing FasterOS[multi] vs FasterOS[list comprehension]')
# faster_os_multi_faster_os.run()
