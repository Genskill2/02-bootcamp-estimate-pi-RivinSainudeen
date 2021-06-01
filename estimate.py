import random
import math

def wallis(n):
	t = 1 
	for i in range (1,n+1):
		t = t * 4 * (i*i) / (4*(i*i) - 1)
	return t * 2
	
def monte_carlo(n):
	i = 0
	c = 0 #points inside circle - counter
	s = 0 #points outside circle - counter
	while i <= n:
		xy = [random.random(), random.random()] #random co-ordinates
		r = math.sqrt(xy[0] * xy[0] + xy[1] * xy[1]) 
		if r < 1:
			c = c + 1
			s = s + 1
		else:
			s = s + 1
		i = i + 1
	return 2 * 4 * c / (c+s)
	
