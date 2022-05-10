
def run():
    #number_square = []

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         number_square.append(i**2)
    
    
    number_square = [i**2 for i in range(1,101) if i % 3 != 0]
    
    print(number_square)


if __name__ == '__main__':
    run()