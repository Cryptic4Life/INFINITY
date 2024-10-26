stock = {
    "tecido": 2200,
    "algodão": 2200,
    "fio": 2200,
    "poliéster": 2200
}

def remove_product(list_of_products, name):
    list_of_products.remove(name)
    return 0

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