import random
import math

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
	
