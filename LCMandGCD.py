def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
def lcm(a,b):
    return (a/gcd(a,b))*b
a=int(input("Enter the value of 'A':"))
b=int(input("Enter the value of 'B':"))
print("LCM of",a,"and",b,"is",lcm(a,b))
print("GCD(HCF) of",a,"and",b,"is",gcd(a,b),"\n")
