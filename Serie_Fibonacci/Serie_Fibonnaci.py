#Definimos funcion de bucle para ejecutar el programa
def serie():
    #Introducimos un numero para calcular el Fibonacci del mismo
    valor = int (input("Introduce numero a calcular: "))
    # traemos y enviamos el valor 
    resultado = fibonacci (valor)
    # Imprimimos el retorno del valor
    print ("Su resultado en la serie Fibonacci es: " + str (resultado))
# se realiza una funcion de ciclo FOR para calcular la serie Fibonnaci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        for i in range (1,n): 
            return (fibonacci(n-1) + fibonacci(n-2))

#Iniciamos como buena practica para Python
if __name__ == "__main__":
    serie ()
    
