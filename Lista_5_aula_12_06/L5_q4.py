def primo(limite):
    for num in range(0,limite):
        if all(num%i!=0 for i in range(2,num)):
            if num >= 2:
                print(num)
if __name__ == "__main__":
    limite = int(input("limite \t"))
    primo(limite)