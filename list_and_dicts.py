def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Rodrigo", "lastname": "Flores"}
    
    super_list = [
        {"firstname": "Rodrigo", "lastname": "Flores"},
        {"firstname": "Constanza", "lastname": "Hernandez"},
        {"firstname": "Marisol", "lastname": "Pereira"},
        {"firstname": "Sergio", "lastname": "Flores"},
        {"firstname": "Paula", "lastname": "Flores"},              
        ] 
    
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, -0 -1- 2],
        "floating_nums": [1.1, 4.5, 6.43],
    }
    
    for key, value in super_dict.items():
        print(key, "-", value)
        
    for values in super_list:
        for key, items in values.items():
            print(items, end=" ")
        print("", sep="\n")


if __name__ == '__main__':
    run()