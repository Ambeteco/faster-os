from speed_tests.speed import compare_multi
from speed_tests.funcs_map import faster_os_multi_os


def run():
    compare_multi(faster_os_multi_os)
