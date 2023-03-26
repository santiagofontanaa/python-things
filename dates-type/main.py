# En Python existen 4 tipos de datos simples que son utilizados con frecuencia en este lenguaje, estos son Int, Float, Text y Boolean
# El tipo de dato de Texto, conocido como String es basicamente para declarar una palabra o conjunto de palabras, para hacer un string podemos utilizar varias formas como comillas dobles "", comillas simples '', o triple """""", ''''''. 
# Las comillas dobles o simples sirven para hacer una cadena de texto en una sola linea, sin embargo las triples sirven para escribrir en mas de una linea. Aqui un ejemplo

comillas_dobles_simple = "¡Soy un texto de una sola linea!"
comillas_simples_simple = '¡Soy un texto de una sola linea!'

# Aquí podemos ver como no sería su correcto uso:
"""
"
¡Soy un texto de una sola linea!
¡No funciono en dos o mas lineas!
"

'
¡Soy un texto de una sola linea!
¡No funciono en dos o mas lineas!
'
"""

# Aquí podemos ver como sería el correcto uso en caso de querer utilizar dos o mas lineas:
text =  """"
    tus datos son:
        nombre: a
        apellido: a
    """
text =  '''
    tus datos son:
        nombre: a
        apellido: a
    '''

# Otro tipo de dato seria el Int, es decir un numero entero, tales como 1, 10, 100, 1000 y asi infinitamente pero tienen que ser numeros completos que no vayan con una coma (en Python esa coma se representa con un punto, por ejemplo 10.2), recordemos que Python es un lenguaje de tipiado dinamico, es decir que averigua por forma propia si la variable es un Int, Texto, Float o Boolean entonces no hay que declarar que es un numero. Veamos unos ejemplos:

a = 4
b = 5
c = a + b

# El hermano del Int seria el Float, que en vez de ser numeros enteros son numeros que siempre tienen coma (representado con un punto .)
4.4
3.1000
6.23
10000.01

# Por ultimo el mas sencillo de entender seria el Boolean que basicamente declara si es Falso o Verdadero

fui_al_baño = False
hablo_español = True

False
True
