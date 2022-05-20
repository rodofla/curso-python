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
    try:
        num = int(input("Ingresa un número: "))
        if num <= 0:
            raise ValueError
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar 'solo' números enteros positivos")

if __name__ == '__main__':
    run()