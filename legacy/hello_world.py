import logging
from pyats import aetest

logger = logging.getLogger(__name__)

class Testcase(aetest.Testcase):

    @aetest.test
    def hello_world(self):
        # print won't be visible to terminal
        logger.info('Hello World')

if __name__ == '__main__':
    
    logger.setLevel(logging.INFO)
    aetest.main()