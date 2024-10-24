Algoritmo sin_titulo
	Definir frutas Como Caracter 
	Dimension frutas[99]
	Definir cantidades Como Entero
	Dimension cantidades[99]
	Definir opcion, i Como Entero
	Definir cantidad Como Entero
	Dimension cantidad[100]
	Definir articulo Como Caracter
	Definir cantidadFrutas Como Entero
	
	cantidadFrutas <- 0
	
	Mientras Verdadero Hacer
		Escribir "Seleccione una opción:"
		Escribir "1 - Ingresar un artículo (frutas)"
		Escribir "2 - Buscar un artículo"
		Escribir "3 - Imprimir todos los artículos cargados"
		Escribir "4 - Salir"
		Leer opcion
		
		Segun opcion Hacer
			1:
				Si cantidadFrutas <=99 Entonces
					Escribir "Ingrese el nombre de la fruta:"
					Leer frutas[99]
					Escribir "Ingrese la cantidad:"
					Leer cantidades[99]
					cantidadFrutas <- cantidadFrutas + 1
					Escribir frutas[99], " agregado con éxito."
				Sino
					Escribir "Se ha alcanzado el límite de frutas."
				FinSi
				
			2:
				Escribir "Ingrese el nombre de la fruta a buscar:"
				Leer articulo
				encontrado <- Falso
				Para i <- 1 Hasta cantidadFrutas - 1 Hacer
					Si frutas[99] = articulo Entonces
						Escribir frutas[99], ": ", cantidades[99]
						encontrado <- Verdadero
					FinSi
				Fin Para
				Si No encontrado Entonces
					Escribir "Artículo no encontrado."
				FinSi
				
			3:
				Si cantidadFrutas <= 99 Entonces
					Escribir "Artículos cargados:"
			        Para i<- 0 Hasta cantidadFrutas - 1 Hacer
						Escribir frutas[99], ": ", cantidades[99]
					Fin Para
				Sino
					Escribir "No hay artículos cargados."
				Fin Si
				
			4: si opcion =3
					Escribir "Saliendo de la aplicación."
					
			   Fin si
				
			
			  De Otro Modo:
				Escribir "Opción no válida, por favor intente de nuevo."
		Fin Segun
Fin Mientras
FinAlgoritmo
