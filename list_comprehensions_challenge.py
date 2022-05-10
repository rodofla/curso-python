def run():
# Encuentra, agrega a una lista e imprime los primeros 1000 números
# naturales que sean multiplos de 4,6 y 9
    square = []
    
    for i in range(1, 1001):
        if i % 4 == 0 and i % 6 == 0 and i % 9 == 0:
            square.append(i)
        
    print(square)

# hace lo mismo pero ocupamos el MCM  de 4, 6 y 9 para realizar la
# operación, ahorrando así código.
    squares_2 = []
    
    for i in range(1, 1001):
        if i % 36 == 0:
            squares_2.append(i)
    
    print(squares_2)
    

#lo mismo que el ciclo for anterior pero con list comprehensions
    squares_3 = [i for i in range(1, 1001) if i % 36 == 0]
    print(squares_3)
    

if __name__ == '__main__':
    run()