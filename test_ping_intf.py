import re
import logging
from pyats import aetest

logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def set_topology(self,
                       testbed,
                       ios1_name='csr1000v-1'):
        ios1=testbed.devices[ios1_name]

        self.parent.parameters.update(ios1 = ios1)

    @aetest.subsection
    def connect(self, steps, ios1):
        with steps.start(f'Connecting to {ios1}'):
            ios1.connect()

# @aetest.loop(device=())
class PingTestcase(aetest.Testcase):

    device = 'ios1'
    destination='20.30.40.50'

    @aetest.test
    def ping_intf(self, device=device, destination=destination):
        try:
            result = self.parameters[device].ping(destination)
        except Exception as e:
            self.failed(f"Ping {destination} from device {device} failed with error: {e}", goto = ['exit'])
        else:
            match = re.search(r"Success rate is (?P<rate>\d+) percent", result)
            success_rate = match.group("rate")

            logger.info(f"Ping {destination} with success rate of {success_rate}")

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self,steps,ios1):
        with steps.start(f"Disconnecting from {ios1.name}"):
            ios1.disconnect()

if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser(description = "AETEST -- Ping Test")
    parser.add_argument('--testbed', dest = 'testbed', type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
