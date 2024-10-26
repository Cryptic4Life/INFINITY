filename = input();

with open("encomenda1.txt") as f:
    for line in f:
        quantidade, tipo, tamanho = line.split(" ")
        print(quantidade)
        print(tipo)
        print(tamanho)