nombre = ""
veces=0
contador=0
nombre= input( "cual es su nombre? :")
veces= int(input("cuantas veces quiere que se imprima su nombre? : "))
while not contador >=veces:
    contador = contador + 1
    print(nombre)