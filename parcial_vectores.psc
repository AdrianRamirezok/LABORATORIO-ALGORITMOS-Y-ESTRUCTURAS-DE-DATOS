Algoritmo parcial_vectores_matrices
	Definir cantidad, i, numero, mayor, menor, contadorMayorQue5, suma Como Entero
	
	Escribir "Ingrese la cantidad de n�meros a evaluar:"
	Leer cantidad
	
	mayor = 0
	menor = 0  
	contadorMayorQue5 = 0
	suma = 0
	Para i Desde 1 Hasta cantidad Hacer
		Escribir "Ingrese el n�mero ", i, ":"
		Leer numero
		
		
		Si numero > mayor Entonces
			mayor = numero
		FinSi
		
		Si numero < menor Entonces
			menor = numero
		FinSi
		
	
		Si numero > 5 Entonces
			contadorMayorQue5 = contadorMayorQue5 + 1
		FinSi
		
		
		suma = suma + numero
	Fin Para
	Escribir "El mayor n�mero ingresado es: ", mayor
	Escribir "El menor n�mero ingresado es: ", menor
	Escribir "La cantidad de n�meros ingresados mayores que 5 es: ", contadorMayorQue5
	Escribir "La suma de todos los n�meros es: ", suma	
	
	
	
FinAlgoritmo
