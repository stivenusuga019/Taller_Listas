departamentos_colombia = []

for x in range(int(input("Escriba numero de departamentos de colombia que desea ingresar: "))):
    dep= (input("Ingrese departamentos: "))
    departamentos_colombia.append(dep)

print("los ultimos 2 departamentos Ingresados son: ",{departamentos_colombia[-2]},{departamentos_colombia[-1]})

departamentos_colombia.sort(reverse=True)
print(departamentos_colombia)
print("la cantidad de elementos que hay en lista son :",len(departamentos_colombia))