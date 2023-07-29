from feature_usage import MathTest

class RealMathTest(MathTest):

    uid = 'rocket_science_math_test'
    groups = ('elementary', 'basic')

    a = 1
    b = 2

if __name__ == '__main__':
    RealMathTest