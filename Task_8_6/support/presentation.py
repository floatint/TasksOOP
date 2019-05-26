def strpoly(poly):
	coef_cnt = len(poly.c)-1 # кол-фо коэфицентов
	str_poly = r'P_{}(x)='.format(coef_cnt) # строковое представление полинома

	for i in range(coef_cnt):
		str_poly += '-' if poly.c[i] < 0 else '' if i == 0 else '+'
		str_poly += str(abs(poly.c[i]))
		str_poly += 'x^'+str(coef_cnt - i) if coef_cnt - i > 1 else 'x'
	return str_poly