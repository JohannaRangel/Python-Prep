#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]: 
num= 8
print(num)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
con=8.5
type(con)


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
type(num)


# 4) Crear una variable que contenga tu nombre

# In[2]:
mi_nombre= 'Johanna Rangel'


# 5) Crear una variable que contenga un número complejo

# In[3]:
num_comp= 7 + 2j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
type(num_comp)


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
var_1= 'True'
var_2= True


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(var_1))
print(type(var_2))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
v_sum= 7 + 2.4


# 11) Realizar una operación de suma de números complejos

# In[2]:
comp1= 5 + 5j
comp2= 1 + 7j
sum_comp= (comp1 + comp2)
print(sum_comp)


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
int1= 6
comp1= 4 + 6j
print(int1 + comp1)


# 13) Realizar una operación de multiplicación

# In[5]:
print(6 * 2)


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
n_co= (27/4)
print(n_co)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print(int(n_co))


# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(27 % 4)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
var= 4 * 6 + 3
print(var) 


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
var_1= 'Hola '
var_2= 'Henry'
print(var_1 + var_2)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
print(2 == "2")


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
print(2 == int("2"))


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
#a = float('3,8')
#no se puede convertir un string en flotante


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
var = 3     
var -= 1
print(var)                   


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
print(1 << 2) 
#el numero 1 en binario se representa 0001
#El binario 0001 se desplaza 2 posiciones hacia la izquierda y se rellena con ceros a la derecha quedando 0100 que representa al decimal 4

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
#print(2 + '2') #da error porque son un entero y un string


# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
var1= 'Sigo estudiando '
var2= 2
print(var1 * var2)


