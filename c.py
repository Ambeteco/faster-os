from timeit import timeit
from win.test_paths import join_paths
import faster_os

faster_os.path.multi_join_list(join_paths)
faster_os.path.multi_join(join_paths)

join_paths *= 10

print('_list', timeit(lambda: faster_os.path.multi_join(join_paths), number=5000))
print('_for ', timeit(lambda: faster_os.path.multi_join_list(join_paths), number=5000))
