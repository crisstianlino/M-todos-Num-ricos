import math

def f(x):
	return math.cos(x)
	
def gauss_legendre_2(x_min, x_max, n_particoes):
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
	
def gauss_legendre_3(x_min, x_max, n_particoes):
	a = float(x_min)
	h = (x_max - a)/(int(n_particoes))
	b = a + h
	w1 = 5/9
	w2 = 8/9
	w3 = w1
	x1 = -math.sqrt(3/5)
	x2 = 0
	x3 = math.sqrt(3/5)
	soma_part = 0
	area = 0
	for i in range(n_particoes):
		area = (b-a)/2*(w1*f((b-a)/2*x1 + (b+a)/2) + w2*f((b-a)/2*x2 + (b+a)/2) + w3*f((b-a)/2*x3 + (b+a)/2))
		soma_part = soma_part + area
		a = b
		b = b + h
	return soma_part
	
def gauss_legendre_4(x_min, x_max, n_particoes):
	a = float(x_min)
	h = (x_max - a)/(int(n_particoes))
	b = a + h
	w1 = (18+math.sqrt(30))/36
	w2 = w1
	w3 = (18-math.sqrt(30))/36
	w4 = w3
	x1 = math.sqrt((3-2*math.sqrt(6/5))/7)
	x2 = -math.sqrt((3-2*math.sqrt(6/5))/7)
	x3 = math.sqrt((3+2*math.sqrt(6/5))/7)
	x4 = -math.sqrt((3+2*math.sqrt(6/5))/7)
	soma_part = 0
	area = 0
	for i in range(n_particoes):
		area = (b-a)/2*(w1*f((b-a)/2*x1 + (b+a)/2) + w2*f((b-a)/2*x2 + (b+a)/2) + w3*f((b-a)/2*x3 + (b+a)/2) + w4*f((b-a)/2*x4 + (b+a)/2))
		soma_part = soma_part + area
		a = b
		b = b + h
	return soma_part
	
def gauss_legendre_5(x_min, x_max, n_particoes):
	a = float(x_min)
	h = (x_max - a)/(int(n_particoes))
	b = a + h
	w1 = 128/225
	w2 = (322+13*math.sqrt(70))/900
	w3 = w2
	w4 = (322-13*math.sqrt(70))/900
	w5 = w4
	x1 = 0
	x2 = 1/3*math.sqrt(5-2*math.sqrt(10/7))
	x3 = -x2
	x4 = 1/3*math.sqrt(5+2*math.sqrt(10/7))
	x5 = -x4
	soma_part = 0
	area = 0
	for i in range(n_particoes):
		area = (b-a)/2*(w1*f((b-a)/2*x1 + (b+a)/2) + w2*f((b-a)/2*x2 + (b+a)/2) + w3*f((b-a)/2*x3 + (b+a)/2) + w4*f((b-a)/2*x4 + (b+a)/2) + w5*f((b-a)/2*x5 + (b+a)/2))
		soma_part = soma_part + area
		a = b
		b = b + h
	return soma_part
	
print(gauss_legendre_5(0,math.pi/2,1))
		
