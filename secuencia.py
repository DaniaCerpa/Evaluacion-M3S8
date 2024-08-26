
lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]


#Impresión de cada dato
print("Impresión de cada dato excluyendo el cero y cada sublista empezando en cero:")
for sublista in lista:
    if sublista [0]==0:
        continue
    for numero in sublista:
        if numero == 0:
            continue
        else: 
            print (numero) 


print ()

#Creación de diccionario

print("Impresión de items en diccionario creado con listas:")
diccionario = {"A:": lista[0], "B:": lista[1], "C:": lista[2], "D:": lista[3]}

for clave, valor in diccionario.items():
    print (clave, valor)



