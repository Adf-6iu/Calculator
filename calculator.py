import time, os
os.system('cls')
print("*************************************")
print("* [1] Calculator                    *")
print("* [2] Float Calculator              *")
print("* [3] Exit                          *")
print("*************************************")
A = int(input("\n$ "))
if A == 1:
    print("_______________________________")
    print("[1] +                         |")
    print("[2] -                         |")
    print("[3] ×                         |")
    print("[4] ÷                         |")
    print("[5] <                         |")
    print("[6] >                         |")
    print("______________________________|")
    B = int(input("\n$ "))
    if B == 1:
        print("Type First Number:") 
        C = int(input("\n$ "))
        print("Type Second Number:")
        D = int(input("\n$ "))
        E = C + D
        print("---------------------")
        print(E)
        time.sleep(10)
    elif B == 2:
        print("Type First Number:")
        F = int(input("\n$ "))
        print("Type Second Number:")
        G = int(input("\n$ "))
        H = F - G
        print("---------------------")
        print(H)
        time.sleep(10)
    elif B == 3:
        print("Type First Number:")
        I = int(input("\n$ "))
        print("Type Second Number:")
        J = int(input("\n$ "))
        K = I * J
        print("---------------------")
        print(K)
        time.sleep(10)
    elif B == 4:
        print("Type First Number:")    
        L = int(input("\n$ ")) 
        print("Type Second Number:")
        M = int(input("\n$ "))
        N = L / M
        print("--------------------")
        print(N)
        time.sleep(10)
    elif B == 5:
        print("Type First Number:")  
        O = int(input("\n$ "))
        print("Type Second Number:")
        P = int(input("\n$ "))
        Q = O < P
        print("---------------------")
        print(Q)
        time.sleep(10)
    elif B == 6:
        print("Type First Number:")  
        R = int(input("\n$ "))
        print("Type Second Number:")
        S = int(input("\n$ "))
        T = R > S
        print("---------------------")
        print(T)
        time.sleep(10)
    else:
        print(B, "Not Command For This Tool")
elif A == 2:
    print("_______________________________")
    print("[1] +                         |")
    print("[2] -                         |")
    print("[3] ×                         |")
    print("[4] ÷                         |")
    print("[5] <                         |")
    print("[6] >                         |")
    print("______________________________|")
    b = int(input("\n$ "))
    if b == 1:
        print("Type First Number:")
        c = float(input("\n$ "))
        print("Type Second Number:")
        d = float(input("\n$ "))
        e = c + d
        print("----------------------")
        print(e)
        time.sleep(10)
    elif b == 2:
        print("Type First Number:")
        f = float(input("\n$ "))
        print("Type Second Number:")
        g = float(input("\n$ "))
        h = f - g
        print("----------------------")
        print(h)
        time.sleep(10)
    elif b == 3:
        print("Type First Number:")
        i = float(input("\n$ "))
        print("Type Second Number:")
        j = float(input("\n$ "))
        k = i * j
        print("----------------------")
        print(k)
        time.sleep(10)
    elif b == 4:
        print("Type First Number:")
        l = float(input("\n$ "))
        print("Type Second Number:")
        m = float(input("\n$ "))
        n = l / m
        print("----------------------")
        print(n)
        time.sleep(10)
    elif b == 5:
        print("Type First Number:")
        o = float(input("\n$ "))
        print("Type Second Number:")
        p = float(input("\n$ "))
        q = o < p
        print("----------------------")
        print(q)
        time.sleep(10)
    elif b == 6:
        print("Type First Number:")
        r = float(input("\n$ "))
        print("Type Second Number:")
        s = float(input("\n$ "))
        t = r > s
        print("----------------------")
        print(t)
        time.sleep(10)
    else:
        print(B, "Not Command For This Tool")
elif A == 3:
    exit()
else:
    print(A, "Not Command For This Tool")