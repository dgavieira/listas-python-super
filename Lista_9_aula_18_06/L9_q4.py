with open("teste.txt") as f:
    with open("copia.txt", "w", encoding="utf-8") as f1:
        for line in f:
            f1.write(line)