'''print("Hola Mundo")
lista = []
for i in range(10):
    print("Hola Mundo")
    lista.append(i)
for i in range(10):
    print(lista[i])
diccionario = {'Estudiante1' : 'Luis', 'Estudiante2' : 'Isaac', 'Estudiante3' : 'Xime', 'Estudiante4' : 'Andy'} 
print(diccionario['Estudiante1'])'''

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Seleccione la operación.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")

while True:
    # Take input from the user
    choice = input("Ingrese la opción(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Eleccion no valida")