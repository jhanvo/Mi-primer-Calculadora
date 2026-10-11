print("¡Hola, Bienvenido a la Mini Calculadora!")

numero_uno = int(input("Escribe el primer número: "))
numero_dos = int(input("Escribe el segundo número: "))

print("La suma es: ", numero_uno + numero_dos)
print("La resta es: ", numero_uno - numero_dos)
print("La multiplicación es: ", numero_uno * numero_dos)
if numero_dos == 0:
    print("No se puede dividir entre cero")
else:
    print("La división es: ", numero_uno/numero_dos)

