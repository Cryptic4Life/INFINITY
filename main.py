filename = input();

with open(filename) as f:
    for line in f:
        quantidade, tipo, tamanho = line.split(" ")
        print(quantidade)
        print(tipo)
        print(tamanho)