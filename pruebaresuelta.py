import math 
opc='s'
while opc=='s':
	operacion = raw_input ('Que desea Calcular1:longitud cadena de caracter, 2: raiz cuadrada ')
	if operacion =='1':
		longitud= raw_input ('ingrese cadena de caracteres')
		print ('la cadena tiene', len(longitud),'caracteres')
	elif operacion=='2':
		raiz= input ('ingrese numero cuya raiz quiere calcular'))
		print ('la raiz del numero que ingreso es: ',math.sqrt(raiz) )
	else:
		(print ('ingreso una opcion que no es valida'))
		opc= (input ('desea volver a intentarlo s/n'))
		#Vargas Leidymar C.I 22.883.946