huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}

# Imprime las claves y los valores.
print (huespedes)
#Se convierte en una lista.
print (huespedes.items())

# Imprime solo las claves.
print (huespedes.keys())
for key in huespedes:
    # Imprime las claves una bajo la otra.
    print (key)

# Imprime unicamente los valores.
print (huespedes.values())
for key in huespedes:
    # Imprime los valores uno bajo el otro.
    print (huespedes[key])
print()

for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion])
    #Hace que las claves cambien a "Habitacion" y los valores a "huspedes" imprimiendo una simulacion de habitacion para su respectivo huesped.
print()

for habitacion,huesped in huespedes.items():
    #Imprime en todos las claves un mismo valor.
    print (habitacion,':',huespedes[key])

for indice, key in enumerate(huespedes):
    print (indice+1,key,huespedes[key])
    # Se suma 1 antes de las claves y los valores para crear una lista de 1 a 3 con la habitacion y huesped correspondiente
print()

print (huespedes[105])
#Imprime el valor 105 (Paquita la del Barrio)
print (huespedes.get(105))

print ('-------------------------------------')

huespedes[102]='Fanny Lu'
huespedes[107]='Don Omar'
#Se añadio nuevas claves y valores al diccionario.
huespedes.setdefault('109','Luis Miguel')

for huesped in huespedes.items():
    print (habitacion,':',huesped)
    #Imprime los nuevos huspedes y diccionarios como si estuvieran registrados en un mismo "recibo" pero con su diferencia de clave y valor siguen.
print()

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}
huespedes.update(registroshoy)
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped)
    #Imprime nuevas claves y valores.
print()

print ('-------------------------------------')

huespedes[107]='Ricky Martin'
print (huespedes)
#Añade una nueva clave y valor dentro de los existenten en orden de menor a mayor utilizando el numero designado en la clave.
print ('-------------------------------------')

del huespedes[102]
huespedes.pop(202)
print(huespedes)
# ¿Imprime las claves impares?
print ('-------------------------------------')

copia1=huespedes.copy()
print ('copia1: ',copia1)
copia2={}
copia2.update(huespedes)
print ("copia2: ",copia2)
# Crea dos copias de la lista de impares.
print ('-------------------------------------')

lista=[2,5,7,1]
diccio=dict.fromkeys(lista,"xxx")
print(diccio)
# Crea 4 claves con su respectivo valor.
print ('-------------------------------------')

inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}
print (inventario)
#Imprime la seccion de "cartera" en orden alfabetico
inventario["cartera"].sort()

print(inventario)
#Imprime la clave.
print(inventario.get("plata")[0])