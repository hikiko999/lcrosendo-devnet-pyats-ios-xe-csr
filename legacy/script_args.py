import logging
from pyats import aetest

logger = logging.getLogger(__name__)

class Testcase(aetest.Testcase):

    @aetest.test
    def script_arg(self,testbed,vlan):
        # print won't be visible to terminal
        logger.info(f'Testbed = {testbed}')
        logger.info(f'VLAN = {vlan}')


if __name__ == '__main__':
    
    logger.setLevel(logging.INFO)

    import sys
    import argparse
    from pyats.topology import loader
    
    # --help description
    parser = argparse.ArgumentParser(description = 'standalone parser')
    # dest is variable it goes into
    parser.add_argument('--testbed', dest = 'testbed')
    parser.add_argument('--vlan', dest = 'vlan')

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    testbed = loader.load(args.testbed)
    vlan = int(args.vlan)

    aetest.main(testbed = testbed, vlan = vlan)
    logger.info(f"Sys.arg = {sys.argv[1:]}")
