from math import sqrt as sqrt

def run():
# creamos un diccionario que imprime la llave y el valor solo si 
# la llave no es divisible por 3
    square = {i:i**3 for i in range(1, 101) if i % 3 != 0 }
    print(square)
    print("\n")
    
# creamos un diccionario que imprime la llave y la raíz cuadrada de la llave
# con 1 decimal como valor.  
    square_2 = {i:round(sqrt(i), 1) for i in range(1,1001) }
    print(square_2)


if __name__ == '__main__':
    run()