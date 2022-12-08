def ListaDivisibles(numero, tope):
    '''
    Construir una funcion que devuelva una lista 
    ordenada de menor a mayor con los numeros 
    divisibles por el parametro numero entre 1 y el
    valor del parametro "tope"
    Recibe dos argumentos
    numero: numero entero divisor
    tope: maximo valor a evaluar a partir de 1

    ej:

    LstaDivisibles(6,30) debe retornar [6,12,18,24,30]
    LstaDivisibles(10,5) debe retornar []
    LstaDivisibles(7,5) debe retornar [7,14,21,28,35,42,49]
    '''
    multiplos_divisibles_number = []
    add_number = int()
    for i in range(1,tope+1):
        resultado_resto = i % numero
        if resultado_resto == 0 :
            add_number = i
            multiplos_divisibles_number.append(add_number)
            multiplos_divisibles_number.sort(reverse=False)
    print(multiplos_divisibles_number)
    return multiplos_divisibles_number



#ListaDivisibles(6,30)
#ListaDivisibles(10,5) 
#ListaDivisibles(7,50)

# REUSLTADOS ARROJADOS OK; NO CHEQUEADOS CON EL TEST



def Exponente(numero, exponente):
    '''
    Esta función devuelve el resultado de elevar el parámetro "número"
    al parámetro "exponente"
    Recibe 2 parametros:
    Número: numero afectado al exponente
    Exponente: numero exponente en la operación exponencial
    '''
    resultado_funcion_exponencial = numero ** exponente
    print(resultado_funcion_exponencial)
    return resultado_funcion_exponencial
    

#Exponente(10,3)




def ListaDeListas (lista):
    '''
    Esta función recibe una lista, que puede contener 
    elementos que a su vez sean Listas y devuelve esos elementos
    por separado en una lista unica.

    En caso de que el parametro no sea un tipo de lista, debe retornar nulo.
    
    Recibe un Argumento:
    Lista: La lista que puede contener otras listas
    y se convierte a una lista de elementos
    únicos no iterables.

    Ej:
    ListaDeListas([1,2],['a','b','c'], [10])
    ListaDeListas(108) . debe retornar null
    ListaDeListas([1,2,[3],[4]],['a','b','c'], [10])
    '''
    listafinal = []
    
    if type(lista) != list:
        return None
    for elemento in lista:
        if type(elemento) != list:
            listafinal.append(elemento)
        else:
            listafinal.extend(ListaDeListas([elemento]))
    
    print(listafinal)
    return listafinal


#ListaDeListas([[1,2],['a','b','c'], [10]])
#ListaDeListas([[1,2],['a','b','c'], [10]])
#ListaDeListas([[1,2],['a',['c',[1,2,[4],3],'d'],'b','c'], [10]])
#ListaDeListas([[1,2],['a','b','c'], [10]])



def Factorial(numero):
    '''
    Esta funcion devuelve el factorial del nummero pasado como parametro
    en casp de qie mo sea emtero y/o sea menor que 0, debe retornar Nulo
    recibe un argumento:
        numero: sera el numero con el que se calcule su factorial.

    ej:
    Factorial(4) = 24
    Factorial(-2)  debe retornar nulo
    Factorial(0) debe retotnar 1
    '''
    factorial = 1

    if (type(numero) != int()) & (numero < 0):
        return None
    for i in range(1,numero):
        factorial = Factorial(numero-1) * numero
    print(factorial)
    return factorial

#(Factorial(0))
#(Factorial(-2))
#(Factorial(5))





def ListaPrimos(desde, hasta):
    '''
    Esta funcion devuelve una lista con los numeros primos entre los valores
    "desde" y "hasta" pasados como parámetros siendo ambos inclusivos!
    
    En caso de e algunoo de los parametros no sea de tipo enterio y/o no sea mayor a cero, 
    debe retornar nulo.
    
    En caso de que el segundo parametro sea menor al primero, pero ambos mayores que cero, 
    debe retornar una lista vacía.

    Recibe un Argumento:
    desde: sera el numero a partir del cual se toma el rango.
    hasta: sera el numero hasta el cual se tome el rango

    ej
    ListaPimos(7,15) debe retornar [7,11,13]
    ListaPimos(100,99) debe retornar []
    ListaPrimos(1,7) debe retornar [1,2,3,5,7]
    '''
    false_list = []

    if ((type(desde) != int) & (desde < 0)):
        return None
    elif type(hasta) != type(desde):
        return None
    elif desde > hasta:
        return false_list  
    else:
        true_list = list(range(desde,hasta+1))
        listaprim = []
        es_primo = True
        for elemento in true_list:
            for i in range(2,elemento):
                if (elemento % i == 0):
                    es_primo = False
                    break
                else:
                    listaprim.append(elemento)
                    break
    print(listaprim)                
    return listaprim

#ListaPrimos(7,15)
#ListaPrimos(7,80)
#ListaPrimos(-7,15)
#ListaPrimos(15,7)
#ListaPrimos(99,100)




def ListaRepetidos(lista):
    '''
    Esta funcion recibe como parámetro una lista y devuelce una lista de tuplas
    donde cada tupla contiene un valor de la lista original y las veces que se repite.
    
    Los valores de la lista original no deben estar repetidos.
    Debe respetarse el orden original en el que aparecen los elementos
    En caso de que el parametro no sea de tipo lista debetornar nulo,
    
    Recibe un argumento
        Lista: será la lista que se va a evaluar.
    
    ej:
    ListaRepetidos([]) retorna []
    ListaRepetidos(['hola','mundo','hola',13,14]) retorna [('hola',2),('mundo',1),(13,1),(14,1)]
    '''
    lista_analizados = []
    lista_cant_repeticiones = []
    
    if type(lista) != list:
        return None
   
    # que recorra la lista y vaya guardando aquellos datos encontrados NO repetidos en lista_anallizados

    for elemento in lista:
        if elemento not in lista_analizados:
            lista_analizados.append(elemento)
        # cree una lista de valores no repes...
        # #ahora por cada vez que aparezca un elemento de la lista de los ya analizados en lista. sume 1 a cantidad de repes.
        else:
            pass
    
    salida_pantalla = print('La lista correspondiente a los diferentes items encontrados es: ' )
    print(lista_analizados)
    
            #version 1
    #Lo que se debe hace es que por cada elemento de la lista ya analizado,
    for e in lista_analizados:

        # Agregue a la lista de "cantidad de repeticiones", la cantidad de veces que encuentra el valor elemento en la lista.
        veces_q_aparece = lista.count(e)
        lista_cant_repeticiones.append (veces_q_aparece)

    # entonces hasta aqui voy a tener 2 listas, lista_analizados y veces_que_aparece

    salida_pantalla = print('La lista correspondiente a las veces que aparecen los elementos es: ' )
    print(lista_cant_repeticiones)

    tuplareturn = list(zip(lista_analizados, lista_cant_repeticiones))
    
    print(tuplareturn)
    return tuplareturn

#(ListaRepetidos(['hola','mundo','hola','hola','HOLA',13,11,1,1,1,1,1,2,2,2,13,14]))


class Vehiculos:
    '''
    Clase vehiculos
    '''
    def __init__(self,tipo, color,velocidad = 0.0):

        self.tipo = tipo
        self.color = color
        self.velocidad = velocidad = float(0.0)

    def Acelerar(self,valuevelocityup,velocidad = 0.0):

        if (self.velocidad + valuevelocityup) < 0:
            velocidad = self.velocidad = 0
            print('Se ha incrementado la velocidad del vehiculo a: ')
            print(self.velocidad)
            print('El incremento fue de:')
            print(valuevelocityup)
            return  velocidad , valuevelocityup

        if (self.velocidad + valuevelocityup) > 100:
            velocidad = self.velocidad = 100
            print('Se ha incrementado la velocidad del vehiculo a: ')
            print(self.velocidad)
            print('El incremento fue de:')
            print(valuevelocityup)
            return  velocidad , valuevelocityup

        if (0 < (self.velocidad + valuevelocityup) < 100):
            self.velocidad = velocidad + valuevelocityup
            print('Se ha incrementado la velocidad del vehiculo a: ')
            print(self.velocidad)
            print('El incremento fue de:')
            print(valuevelocityup)
            return  self.velocidad 

    def propiedades(self,tipo,color,velocidad):
        print(list([tipo,color,velocidad]))
        return(list([tipo,color,velocidad]))

def ClaseVehiculo(tipo,color):
    """
        Esta función devuelve un objeto instanciado de la clase Vehiculo,
        la cual debe tener los siguientes atributos

        Atributos:
            Tipo:       Un valor dentro de los valores posibles['auto','camioneta','moto']
            Color:      Un valor de tipo de dato str()
            Velocidad:  un valor de tipo de dato float(), que debe inicializarse en cero.

        y debe poseer el siguiente método: 
        
        Metodos:
            Acelerar(): Este método recibe un parámetro con el valor
                        que debe incrementar a la propiedad Velocidad y luego retornarla

                        Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
                        Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.

        Recibe 2 argumentos:
            Tipo: dato que se asignará al atributo tipo del objeto de la clase Vehículo.
            Color: dato que se asignará al atributo color del objeto de la clase Vehículo.
            
        ej:
        a = claseVehiculo('auto','gris')
        a.Acelerar(10)
        a.Acellerar(15)
        a.acelerar(-10)

    """

    lista_de_tipos_de_vehiculos_admitidos = ['auto','camioneta','moto']
    tipo = tipo
    color = color
    class Vehiculo:
        '''
        Clase vehiculos
        '''
        def __init__(self,tipo, color,velocidad = 0.0):

            self.tipo = tipo
            self.color = color
            self.velocidad = velocidad = float(0.0)

        def Acelerar(self,valuevelocityup,velocidad = 0.0):

            if (self.velocidad + valuevelocityup) < 0:
                velocidad = self.velocidad = 0
                print('Se ha incrementado la velocidad del vehiculo a: ')
                print(self.velocidad)
                print('El incremento fue de:')
                print(valuevelocityup)
                return  velocidad , valuevelocityup

            if (self.velocidad + valuevelocityup) > 100:
                velocidad = self.velocidad = 100
                print('Se ha incrementado la velocidad del vehiculo a: ')
                print(self.velocidad)
                print('El incremento fue de:')
                print(valuevelocityup)
                return  velocidad , valuevelocityup

            if (0 < (self.velocidad + valuevelocityup) < 100):
                self.velocidad = velocidad + valuevelocityup
                print('Se ha incrementado la velocidad del vehiculo a: ')
                print(self.velocidad)
                print('El incremento fue de:')
                print(valuevelocityup)
                return  self.velocidad 

        def propiedades(self,tipo,color,velocidad):
            return(list([tipo,color,velocidad]))


    if tipo not in lista_de_tipos_de_vehiculos_admitidos:
        print('Error, para esta clase, tipo de vehiculo, solo se admiten los siguientes tipos de vehiculos: ')
        print(lista_de_tipos_de_vehiculos_admitidos)
        return None
    else: 
        tipo = tipo
    if type(color) != str:
        print('Error, para esta clase, color, solo se admite un str() en "color".')
        return None
    else:
        color = color
    
    a1 = Vehiculo(tipo,color)
    print(a1)
    print(a1.color)
    print(a1.velocidad)
    print(a1.tipo)
    incremento_vel = 129
    print(a1.Acelerar(incremento_vel))
    print(a1.propiedades)
    return a1

#auto = 'auto'
#black = 'black'
#print (ClaseVehiculo((auto),(black)))

        



def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, ok
    cuyas listas de valores tienen el mismo tamaño y sus elementos enésimos están asociados. ok
    Y otros dos parámetros que indican la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la relación entre los elementos enésimos.
    
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    

    K.O.

    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    
    Ej:
        dicc = {'clave1':   ['c','a','b'],
                'clave2':   ['casa','auto','barco'],
                'clave3':   [1,2,3]}
                OrdenarDiccionario(dicc, 'clave1')
                                                            debe retornar{  'clave1':   ['a','b','c'],
                                                                            'clave2':   ['auto','barco','casa'],
                                                                            'clave3':   [2,3,1]
                                                                            }


        OrdenarDiccionario(dicc, 'clave3', False)
        
                                            debe retornar {     'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]
                                                                }
    '''
    #Tu código aca:

    # 1. El parametro recibido es un diccionario y o el parametro clave no se encuentra dentro del diccionario.
    
    if (clave not in diccionario_par):
        print('la clave ingresada no existe dentro del diccionario. ')
        return None
    
    listet = list(diccionario_par.keys())
    
    for i in diccionario_par:
        
        if i == clave:
            
            for j in diccionario_par:
                diccionario_par[j].sort()
                
                if descendente == True:
                    diccionario_par[j].reverse()
    
    print(diccionario_par)
    return diccionario_par

dicci = {  

       'clave1':   ['c','a','b'],
                'clave2':   ['casa','auto','barco'],
                'clave3':   [1,2,3]
                                                                                        }

#clave = 'clave3'
#print(type(dicci))
#OrdenarDiccionario(dicci,'clave3',True)


    













