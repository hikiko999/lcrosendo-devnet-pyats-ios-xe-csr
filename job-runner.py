import os
from pyats.easypy import run

def main():
    destinations = os.environ.get("DEST_IP")
    run('test_ping_intf.py', destinations = destinations.split(','))

    # pyats run job job-runner.py --testbed-file ios_testbed.yml --html-logs