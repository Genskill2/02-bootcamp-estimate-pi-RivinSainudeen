import random
import math
import unittest

def wallis(n):
	t = 1.0 
	for i in range (1,n+1):
		t = t * 4.0 * (i*i) / (4.0 * (i*i) - 1)
	return t * 2.0
	
def monte_carlo(n):
	i = 0
	c = 0 #points inside circle - counter
	s = 0 #points inside square - counter
	while i <= n:
		xy = [random.randrange(-1,1), random.randrange(-1,1)] #random co-ordinates
		r = xy[0]**2 + xy[1]**2
		r = math.sqrt(r)
		if r <= 1:
			c = c + 1
			s = s + 1
		else:
			s = s + 1
		i = i + 1
	return 4 * float(c) / float(s)
	

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()


