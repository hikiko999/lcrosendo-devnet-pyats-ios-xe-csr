from pyats import aetest

class MathTest(aetest.Testcase):

    def test_plus(self):
        ''' test requires definitions '''
        assert self.a + self.b < 1000