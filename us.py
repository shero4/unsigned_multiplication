def main():
    multiplicand = input("Enter the multiplicand(Decimal): ")
    m = "{0:b}".format(int(multiplicand))
    print("Number of bits: " + str(len(m)))
    multiplier = input("Enter the multiplier(Decimal): ")
    q = "{0:b}".format(int(multiplier))
    print("Number of bits: " + str(len(q)))
    no_of_bits = int(input("Enter the number of bits: "))
    q = q.zfill(no_of_bits)
    m = m.zfill(no_of_bits)
    n = len(m)
    length = n
    c = "0"
    a = "".zfill(len(m))
    print("INITIALIZATION: ", end="")
    print(c,a,q,m)
    while(n != 0):
        comb = c + a + q
        if(q[-1] == "0"):
            print("Q0 = 0")
            comb = "0" + comb[:-1]
        elif(q[-1] == "1"):
            print("Q0 = 1")
            comb = str(bin(int(a,2) + int(m,2))[2:].zfill(length + 1)) + q
            c = comb[0]
            a = comb[1:1+length]
            q = comb[1+length:]
            comb = c + a + q
            print("A<-A+M:      ", end="")
            print(c,a,q,m)
            comb = "0" + comb[:-1]
        c = comb[0]
        a = comb[1:1+length]
        q = comb[1+length:]
        n = n-1
        print("RIGHT SHIFT: ", end="")
        print(c,a,q,m)
if __name__ == '__main__':
    main()