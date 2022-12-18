
def boleto():
    n = input("Ingrese un número: ")
    if len(n)%2 == 0:
        s1 = 0
        s2 = 0
        for i in range(0,len(n)//2):
            s1 += int(n[i])
        for j in range(len(n)//2,len(n)):
            s2 += int(n[j])

    else:
        s1 = 0
        s2 = 0
        for i in range(0,len(n)//2):
            s1 += int(n[i])
        for j in range(len(n)//2+1,len(n)):
            s2 += int(n[j])

    if s1 == s2:
        print("LUCKY")
    else:
        print("UNLUCKY")
    return n



if __name__ == "__main__":
    print(boleto())