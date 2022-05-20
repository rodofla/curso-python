def divisors(num):
    """
    It takes a number, and returns a list of all the numbers that divide into it
    
    :param num: the number to find the divisors of
    :return: A list of all the divisors of the number.
    """
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0: 
            divisors.append(i)
    return divisors


def run():
    
    num = (input("Ingresa un número: "))
    assert num.isnumeric() and int(num) != 0, "Debes ingresar 'solo' números enteros positivos"    
    print(divisors(int(num)))
    print("Terminó mi programa")    


if __name__ == '__main__':
    run()