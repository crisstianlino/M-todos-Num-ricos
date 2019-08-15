import math

def f(x):
	return math.cos(x)

def regra_trapezio(x_min,x_max,n_particoes):
	a = float(x_min)
	h = (x_max - a)/(int(n_particoes))
	b = a + h
	soma_part = 0
	area = 0
	for i in range(n_particoes):
		area = h*(f(a)+f(b))/2
		soma_part = soma_part + area
		a = b
		b = b + h
	return soma_part
	
def regra_simpson13(x_min,x_max,n_particoes):
	a = float(x_min)
	h = (x_max - a)/(int(n_particoes))
	b = a + h
	p = (a+b)/2
	soma_part = 0
	area = 0
	for i in range(n_particoes):
		area = h/6*(f(a)+4*f(p)+f(b))
		soma_part = soma_part + area
		a = b
		b = b + h
		p = (a+b)/2
	return soma_part
	
def regra_simpson38(x_min,x_max,n_particoes):
	a = float(x_min)
	h = (x_max - a)/(int(n_particoes))
	b = a + h
	p2 = a + (b-a)/3
	p3 = p2 + (b-a)/3
	soma_part = 0
	area = 0
	for i in range(n_particoes):
		area = h/8*(f(a)+3*f(p2)+3*f(p3)+f(b))
		soma_part = soma_part + area
		a = b
		b = b + h
		p2 = a + (b-a)/3
		p3 = p2 + (b-a)/3
	return soma_part
	
def regra_boole(x_min,x_max,n_particoes):
	a = float(x_min)
	h = (x_max - a)/(int(n_particoes))
	b = a + h
	p2 = a + (b-a)/4
	p3 = p2 + (b-a)/4
	p4 = p3 + (b-a)/4
	soma_part = 0
	area = 0
	for i in range(n_particoes):
		area = h/90*(7*f(a)+32*f(p2)+12*f(p3)+32*f(p4)+7*f(b))
		soma_part = soma_part + area
		a = b
		b = b + h
		p2 = a + (b-a)/4
		p3 = p2 + (b-a)/4
		p4 = p3 + (b-a)/4
	return soma_part
	
inicio = float(input("Digite o a: "))
fim = float(input("Digite o b: "))
estrategia = int(input("1 - Escolher número de partições ou 2 - Escolher tolerância: "))
regra = int(input("1 - Trapezio ou 2 - Simpson 1/3 ou 3 - Simpson 3/8 ou 4 - Boole: "))
if regra == 1:
	if estrategia==1:
		n = int(input("Quantas divisões: "))
		integral = float(regra_trapezio(inicio,fim,n))
		print("A integral pela regra do trapézio é: ",integral)
	else:
		tolerancia = float(input("Digite a tolerancia: "))
		integral_anterior = float(regra_trapezio(inicio,fim,1))
		integral_atual = float(regra_trapezio(inicio,fim,2))
		n = 4
		while math.fabs(integral_atual - integral_anterior) > tolerancia:
			integral_anterior = integral_atual
			integral_atual = float(regra_trapezio(inicio,fim,n))
			n = n*2
		print("A integral pela regra do trapézio é: ",integral_atual)
elif regra == 2:
	if estrategia==1:
		n = int(input("Quantas divisões: "))
		integral = float(regra_simpson13(inicio,fim,n))
		print("A integral pela regra de Simpson 1/3 é: ",integral)
	else:
		tolerancia = float(input("Digite a tolerancia: "))
		integral_anterior = float(regra_simpson13(inicio,fim,1))
		integral_atual = float(regra_simpson13(inicio,fim,2))
		n = 4
		while math.fabs(integral_atual - integral_anterior) > tolerancia:
			integral_anterior = integral_atual
			integral_atual = float(regra_simpson13(inicio,fim,n))
			n = n*2
		print("A integral pela regra de Simpson 1/3 é: ",integral_atual)
elif regra == 3:
	if estrategia==1:
		n = int(input("Quantas divisões: "))
		integral = float(regra_simpson38(inicio,fim,n))
		print("A integral pela regra de Simpson 3/8 é: ",integral)
	else:
		tolerancia = float(input("Digite a tolerancia: "))
		integral_anterior = float(regra_simpson38(inicio,fim,1))
		integral_atual = float(regra_simpson38(inicio,fim,2))
		n = 4
		while math.fabs(integral_atual - integral_anterior) > tolerancia:
			integral_anterior = integral_atual
			integral_atual = float(regra_simpson38(inicio,fim,n))
			n = n*2
		print("A integral pela regra de Simpson 3/8 é: ",integral_atual)

elif regra == 4:
	if estrategia==1:
		n = int(input("Quantas divisões: "))
		integral = float(regra_boole(inicio,fim,n))
		print("A integral pela regra de Boole é: ",integral)
	else:
		tolerancia = float(input("Digite a tolerancia: "))
		integral_anterior = float(regra_boole(inicio,fim,1))
		integral_atual = float(regra_boole(inicio,fim,2))
		n = 4
		while math.fabs(integral_atual - integral_anterior) > tolerancia:
			integral_anterior = integral_atual
			integral_atual = float(regra_boole(inicio,fim,n))
			n = n*2
		print("A integral pela regra de Boole é: ",integral_atual)
