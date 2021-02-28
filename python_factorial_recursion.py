#date:28-02-2021
def fac(n):
    return 1 if n == 1 else n*fac(n-1)

n = int(input("Enter the factorial number:"))
print(fac(n))
