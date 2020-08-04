def ler_arquivo():
    try:
        f = open("teste.txt")
        print(f.readlines())
    finally:
        f.close()
        
ler_arquivo()