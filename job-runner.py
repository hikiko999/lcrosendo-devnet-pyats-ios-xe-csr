from pyats.easypy import run

def main():
    run('test_ping_intf.py')

    # pyats run job job-runner.py --testbed-file ios_testbed.yml --html-logs