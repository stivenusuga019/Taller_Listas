numeros_enteros = []

for x in range(int(input("Escriba numero enteros ingresar: "))):
    num= int(input("Ingrese numeros: "))
    numeros_enteros.append(num)


numeros_enteros.sort(reverse=True)
print("decendete",numeros_enteros)
numeros_enteros.sort()
print("acendente",numeros_enteros)

