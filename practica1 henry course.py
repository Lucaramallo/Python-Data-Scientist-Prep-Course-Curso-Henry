#práctica1


#Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

numero_entero = 7
print (numero_entero)

#Imprimir el tipo de dato de la constante 8.5
const85 = 8.5
print(type(const85))

#Imprimir el tipo de dato de la variable creada en el punto 1
print(type(numero_entero))

#Crear una variable con tu cnombre

my_name = 'Luca'

#Crear una variable que contenga un número complejo

num_complex = (3/2)
print (num_complex)

#Mostrar el tipo de dato de la variable crada en el punto 5
print(type(num_complex))

#Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

pi = 4.141592
pi4_decimals = round(pi,4)
print(pi4_decimals)

#Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

string_True = 'True'
realy_true = True
print('is realy that string_true is equal to realytrue? ')

validation = string_True == realy_true
if validation == True:
     print("yeah")
else:
    print("No")

    
#Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print(type(validation))

#Asignar a una variable, la suma de un número entero y otro decimal
num_decimal = 11.55
compuestNumber = numero_entero + num_decimal
print(compuestNumber)

#Realizar una operación de suma de números complejos

punto11 = num_complex + num_complex


#Realizar una operación de suma de un número real y otro complejo

punto12 = numero_entero + num_complex

#Realizar una operación de multiplicación

multiplicacion = numero_entero * num_decimal 
print(multiplicacion)

#Mostrar el resultado de elevar 2 a la octava potencia

dos_ala_octavapotencia = 2 ** 8
print(dos_ala_octavapotencia)


#Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
veinticiete_div_4 = 27/4
print(veinticiete_div_4)

#De la división anterior solamente mostrar la parte entera

veinticiete_div_4_entero = round(veinticiete_div_4)
print(veinticiete_div_4_entero)

#De la división de 27 entre 4 mostrar solamente el resto

only_rest27_div_4 = 27 % 4
print(only_rest27_div_4)

#Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

veinticiete_as_a_result = (veinticiete_div_4_entero + only_rest27_div_4) * 4
print(veinticiete_as_a_result)

#Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas


suma_alfanumericas = 'This is so ' + 'easy'
print(suma_alfanumericas)

#Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
num2 = 2
stringdos = "2"
if num2 == stringdos:
    print("correct")
else:
    print("Not correct")

#Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

convert_tostring_num2 = str(num2)

if convert_tostring_num2 == stringdos:
    print("correct")
else:
    print("Not correct")

#¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

correccionesrror1 = float(3.8)

print(correccionesrror1)
print("se debe a la coma en lugar de .")

#Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenid
#No se necesita crear variable nueva.
tres = 3
tres -= 1
print(tres)

#Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario

expresion = 1 << 2

print(expresion)



#2 << 5  # shift left by 5 bits
        # 0b10 -> 0b1000000
#1000 >> 2  # shift right by 2 bits
           # 0b1111101000 -> 0b11111010
           # el resultado arrojado es desplazar a la derecha 2 bits el número 1.

#¿Qué es el sistema de numeración binario?

#es un sistema de numeración en el que los números son 
# representados utilizando únicamente dos cifras: 
# 0 (cero) y 1 (uno). Es uno de los sistemas que 
# se utilizan en las computadoras,
#  debido a que estas trabajan internamente 
# con dos niveles de voltaje, por lo cual su sistema de 
# numeración natural es el sistema binario.




#Realizar la operación 2 + '2' 
#arroja error

# ¿Por qué no está permitido? 
# In fact, you are adding a string to a number, this is not compatible.

# ¿Si los dos operandos serían del mismo tipo, 
# siempre arrojaría el mismo resultado?
# No.



#Realizar una operación válida entre valores de tipo entero y string
#Arroja error al igual que la anterior.

