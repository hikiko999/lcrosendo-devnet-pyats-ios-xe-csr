from pyats.easypy import run

def main():

    # pyats run job job.py --testbed-file ios_testbed.yml
    # --testbed-file automatically overwrites testbed
    run('script_args.py', vlan = 50)