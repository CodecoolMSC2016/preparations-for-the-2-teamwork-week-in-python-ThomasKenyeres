import unittest

# Here's our "unit".


def IsOdd(n):
	rest = n % 2
	if rest == 0:
		return False
	elif rest == 1:
		return True
	
	


# Here's our "unit tests".


class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
