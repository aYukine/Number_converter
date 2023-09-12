import math

def btoten(n, b): #convert b to base 10
    print("working b2t")
    result = 0
    for i in range(len(n)):
        ten = n[-(i+1)]
        if ten == "A":
            ten = 10
        elif ten == "B":
            ten = 11
        elif ten == "C":
            ten = 12
        elif ten == "D":
            ten = 13
        elif ten == "E":
            ten = 14
        elif ten == "F":
            ten = 15
        else:
            ten = int(ten)

        ten = ten*(b**i)
        result += ten
    return result

def tentob(n, b): #convert 10 to base b
    n = int(n)
    result = ""
    while n > 0:
        i = n%b
        n = math.floor(n/b)
        if i == 10:
            i = "A"
        elif i == 11:
            i = "B"
        elif i == 12:
            i = "C"
        elif i == 13:
            i = "D"
        elif i == 14:
            i = "E"
        elif i == 15:
            i = "F"
        result = result + str(i)
    return result[::-1]


if __name__ == '__main__':
    for i in range(15):
        num = input("Base 10: ")
        print(f"base 2: {tentob(num, 2)}")
        print(f"base 8: {tentob(num, 8)}")
        print(f"base 16: {tentob(num, 16)}")
        print("----------------")