stock = {
    "tecido": 2200,
    "algodão": 2200,
    "fio": 2200,
    "poliéster": 2200
}

PROCURA_ANUAL = 50_000
CUSTO_DE_ENCOMENDA = 10
CUSTO_DE_POSSE = 0.70
PRAZO_DE_ENTREGA = 7
STOCK_DE_SEGURANÇA = 1000

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