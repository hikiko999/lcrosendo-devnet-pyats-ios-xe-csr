import logging
from pyats import aetest

logger = logging.getLogger(__name__)

VLANS = list(range(1,2))

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_testbed(self, testbed):
        '''
        checking testbed information
        '''

        logger.info(f"Testbed = {testbed}")

    @aetest.subsection.loop(vlan=VLANS)
    def configure_vlan(self, vlan):
        '''
        configure every vlan, each being a subsection
        '''
        logger.info(f"configuring vlan: {vlan}")

    @aetest.subsection
    def mark_testcase_for_looping(self, interfaces):
        '''
        marking testcase for looping based on script argument interfaces
        '''
        aetest.loop.mark(InterfaceFlapping, interface = interfaces)

# marked for looping
class InterfaceFlapping(aetest.Testcase):
    '''
    tests interface flapping, requires parameter 'interface'
    '''

    @aetest.setup
    def setup(self, interface):
        logger.info(f'testing interface:{interface}')
    
    @aetest.test.loop(status=['up','down'])
    def test_status(self, status):
        logger.info(f'configure interface status to:{status}')

@aetest.loop(vlan = VLANS)
class Traffic(aetest.Testcase):

    @aetest.setup
    def setup(self, interfaces):
        aetest.loop.mark(self.test, interface = interfaces)

    def test(self, interface, vlan):
        logger.info(f"interface: {interface}")
        logger.info(f"vlan: {vlan}")

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection.loop(vlan=VLANS)
    def unconfigure_vlan(self, vlan):

        logger.info(f"configuring vlan: {vlan}")

if __name__ == '__main__':
    logger.setLevel(logging.INFO)

    import sys
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser(description = "standalone parser")
    parser.add_argument('--testbed', dest='testbed')
    parser.add_argument('--interfaces', dest='interfaces')

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    testbed = loader.load(args.testbed)
    interfaces = args.interfaces.split(',')

    aetest.main(testbed = testbed, interfaces = interfaces)
