#Oscar Manriquez Zavala
datos = [1, [2, [3, [4, 5]]]]
listaAplanada = []
def recorrerLista(datos): 
    for item in datos:
        if type(item) == list: 
            recorrerLista(item) 
        else:
            listaAplanada.append(item) 
          
if type(datos) == list: 
    recorrerLista(datos)
    print(listaAplanada)
else:
    print("No es una lista")

#Notas del Código L = linea.
'''
L4.  Funcion Recursiva para entrar cada que sea una lista
L6.  Si es tipo lista vuelve a llamar a la funcion
L8.  Sino es una lista se agrega a la listaAplanada
L9.  (En caso de pedir datos de entrada) Verificamos que la entrada sea una lista si es una lista manda llamar la funcion recorrerLista 
     sino imprime "No es una lista".
'''

#Pruebas Realizadas
'''
input [] output []
input [1] output [1]
input [1, [2, ["abcd", [4, 5]]]] output [1, 2, 'abcd', 4, 5] Faltaria validar abcd no es un entero
input 1 output No es una lista
'''
