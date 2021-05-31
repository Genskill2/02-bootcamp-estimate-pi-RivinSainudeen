import random
import math

def wallis(n):
	t = 1 
	for i in range (1,n):
		t = t * 4 * (n^2) / (4*(n^2) - 1)
	return t*2
	
def monte_carlo(n):
	i = 0 #iteration counter
	c = 0 #points inside circle - counter
	s = 0 #points outside circle - counter
	while i <= n:
		xy = [random.random(), random.random()] #random co-ordinates
		if math.sqrt(xy[0] ^2 + xy[1] ^2) < 1:
			c = c + 1
		else:
			s = s + 1
	return 4 * c / (c+s)
	
