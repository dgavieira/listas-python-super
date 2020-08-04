def ler_arquivo():
    try:
        f = open("teste.txt")
        for line in f:
            print(line, end = '')
    finally:
        f.close()

ler_arquivo()