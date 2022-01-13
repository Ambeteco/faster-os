import traceback
import win_tests


def run_tests(tests):
    failed = 0

    for i, (name, test_func) in enumerate(tests, 1):
        print(f'\n\n\n--> Running test #{i}/{len(tests)} - {name}')
        try:
            if not test_func():
                print('FAILED')
                failed += 1
        except:
            print('FAILED', traceback.format_exc())
            failed += 1

    if not failed:
        print('----\nSUCCESS!')
    else:
        print(f'----\nFailed {failed}/{len(tests)} tests.')


run_tests(win_tests.tests)
