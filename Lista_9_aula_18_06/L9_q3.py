def criar_arquivo():
    try:
        f = open("mundo_novo.txt",'w', encoding = 'utf-8')
        f.write('seja-bem-vindo')

    finally:
        f.close()

def ler_arquivo():
    try:
        f = open("mundo_novo.txt")
        for line in f:
            print(line, end = '')
    finally:
        f.close()

criar_arquivo()
ler_arquivo()