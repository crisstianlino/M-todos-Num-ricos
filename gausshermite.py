import math

def f(x):
	return math.cos(x)
	
def gauss_hermite_2(x_min, x_max, n_particoes):
	a = float(x_min)
	h = (x_max - a)/(int(n_particoes))
	b = a + h
	soma_part = 0
	area = 0
	for i in range(n_particoes):
		area = (b-a)/2*(f((b-a)/2*-1/math.sqrt(3) + (b+a)/2) + f((b-a)/2*1/math.sqrt(3) + (b+a)/2))
		soma_part = soma_part + area
		a = b
		b = b + h
	return soma_part
