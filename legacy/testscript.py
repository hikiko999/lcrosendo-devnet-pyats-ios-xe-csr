from pyats import aetest

# Base Inhertiance - aetest.CommonSetup
class CommonSetup(aetest.CommonSetup):

    # @aetest.subsection
    # def check_topology(self,
    #                    testbed,
    #                    ios1_name = 'csr1000v-1'):
    #     ios1 = testbed.devices[ios1_name]

    #     self.parent.paremeters.update(ios1 = ios1)

    @aetest.subsection
    def establish_connections(self, steps, ios1):
          with steps.start(f'Connecting to {ios1.name}'):
                ios1.connect()


class PingTestcase(aetest.Testcase):
    
    @aetest.test

class CommonCleanup(aetest.CommonCleanup):
    
    pass