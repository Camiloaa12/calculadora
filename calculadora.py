def es_entero(num):
    """
    Verifica si un número es un entero.
    """
    return isinstance(num, int)

def sumar(a, b):
    """
    Realiza la suma de dos números sin utilizar el operador '+'.
    Se incrementa 'a' mientras se decrementa 'b' hasta que 'b' llegue a cero.
    """
    while b != 0:
        a += 1
        b -= 1
    return a

def restar(a, b):
    """
    Realiza la resta de dos números sin utilizar el operador '-'.
    Se decrementa 'a' mientras se decrementa 'b' hasta que 'b' llegue a cero.
    """
    while b != 0:
        a -= 1
        b -= 1
    return a

def multiplicar(a, b):
    """
    Realiza la multiplicación sin utilizar el operador '*'.
    Se suma 'a' consigo mismo 'b' veces.
    Si uno de los números es negativo, se ajusta el signo del resultado.
    """
    if a == 0 or b == 0:
        return 0
    
    negativo = (a < 0) != (b < 0)  # Determina si el resultado será negativo
    a, b = abs(a), abs(b)

    resultado = 0
    while b > 0:
        resultado = sumar(resultado, a)
        b = restar(b, 1)
    
    return resultado if not negativo else restar(0, resultado)

def dividir(a, b):
    """
    Realiza la división sin utilizar el operador '/'.
    Se realiza restas sucesivas de 'b' en 'a' hasta que 'a' sea menor que 'b'.
    """
    if b == 0:
        return "Error: división por cero"
    
    negativo = (a < 0) != (b < 0)  # Determina si el resultado será negativo
    a, b = abs(a), abs(b)

    cociente = 0
    while a >= b:
        a = restar(a, b)
        cociente = sumar(cociente, 1)

    return cociente if not negativo else restar(0, cociente)

def obtener_entero(mensaje):
    """
    Solicita al usuario un número entero y valida la entrada.
    """
    while True:
        entrada = input(mensaje)
        if entrada.lower() == "salir":
            print("Calculadora finalizada.")
            exit()  # Finaliza el programa inmediatamente
        if entrada.lstrip('-').isdigit():  # Permite números negativos
            return int(entrada)
        else:
            print("Error: Solo se permiten números enteros.")

def obtener_operacion():
    """
    Solicita al usuario una operación válida y la devuelve.
    Si la operación no es válida, se solicita nuevamente.
    """
    operaciones_validas = {"suma", "resta", "multiplicacion", "division", "salir"}
    
    while True:
        operacion = input("Seleccione la operación (suma, resta, multiplicacion, division o 'salir' para finalizar): ").lower()
        if operacion in operaciones_validas:
            if operacion == "salir":
                print("Calculadora finalizada.")
                exit()  # Finaliza el programa inmediatamente
            return operacion
        else:
            print("Error: Operación no válida. Por favor, ingrese una de las siguientes: suma, resta, multiplicacion, division.")

def iniciar_calculadora():
    """
    Inicia la calculadora interactiva que permite realizar operaciones repetidas veces.
    """
    while True:
        print("\nBienvenido a la Calculadora sin Operadores")
        print("Escriba 'salir' en cualquier momento para finalizar.")

        operacion = obtener_operacion()
        num1 = obtener_entero("Ingrese el primer número: ")
        num2 = obtener_entero("Ingrese el segundo número: ")

        if operacion == "suma":
            resultado = sumar(num1, num2)
        elif operacion == "resta":
            resultado = restar(num1, num2)
        elif operacion == "multiplicacion":
            resultado = multiplicar(num1, num2)
        elif operacion == "division":
            resultado = dividir(num1, num2)

        print(f"El resultado es: {resultado}")

        continuar = input("¿Desea realizar otra operación? (sí/no): ").lower()
        if continuar != "si" and continuar != "sí":
            print("Calculadora finalizada.")
            break

def main():
    """
    Función principal que inicia la calculadora cuando el archivo es ejecutado directamente.
    """
    iniciar_calculadora()

if __name__ == "__main__":
    main()