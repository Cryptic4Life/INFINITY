def add_product(list_of_products, name):
    list_of_products.append(name)
    return 0

def remove_product(list_of_products, name):
    list_of_products.remove(name)
    return 0

filename = input();

with open(filename) as f:
    for line in f:
        quantidade, tipo, tamanho = line.split(" ")
        print(quantidade)
        print(tipo)
        print(tamanho)
