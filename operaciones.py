operacion = 0
valor1 = 0
valor2 = 0
result = 0
operacion=input("ingrese una opcion 1. Suma 2. resta 3. multiplicacion 4. division : ")
if operacion == "1":
    valor1 = int(input("ingrese el valor 1: "))
    valor2 = int(input("ingrese el valor 2: "))
    result = valor1+valor2
    print('el resultado de la suma es:', result)

elif operacion =="2":
    valor1 = int(input("ingrese el valor 1: "))
    valor2 = int(input("ingrese el valor 2: "))
    result = valor1-valor2
    print('el resultado de la resta es:', result)

elif operacion =="3":
    valor1 = int(input("ingrese el valor 1: "))
    valor2 = int(input("ingrese el valor 2: "))
    result = valor1*valor2
    print('el resultado de la multiplicacion es:', result)
            

elif operacion =="4":
    valor1 = int(input("ingrese el valor 1: "))
    valor2 = int(input("ingrese el valor 2: "))
    result = valor1/valor2
    print('el resultado de la division es:', result)
                
else:
    print("lo sentimos la opcion que elegiste no existe")


        
