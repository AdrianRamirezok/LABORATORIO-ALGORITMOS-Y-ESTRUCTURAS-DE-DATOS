Algoritmo parcial_vectores_matrices
	Definir cantidad, i, numero, mayor, menor, contadorMayorQue5, suma Como Entero
	
	Escribir "Ingrese la cantidad de números a evaluar:"
	Leer cantidad
	
	mayor = 0
	menor = 0  
	contadorMayorQue5 = 0
	suma = 0
	Para i Desde 1 Hasta cantidad Hacer
		Escribir "Ingrese el número ", i, ":"
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
	Escribir "El mayor número ingresado es: ", mayor
	Escribir "El menor número ingresado es: ", menor
	Escribir "La cantidad de números ingresados mayores que 5 es: ", contadorMayorQue5
	Escribir "La suma de todos los números es: ", suma	
	
	
	
FinAlgoritmo
