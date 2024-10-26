

def add_product(list_of_products, name):
    list_of_products.append(name)

def add_product(list_of_products, name):
    list_of_products.append(name)

def main():
    filename = input()

    with open(filename) as f:
        for line in f:
            quantidade, tipo, tamanho = line.split(" ")
            print(quantidade)
            print(tipo)
            print(tamanho)

if __name__ == main:
    main()