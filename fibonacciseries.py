#fibonacciseries
def fibonacci(n):
    a = 0
    b = 1
    

    if n == 0 :
        print(a)
    elif n == 1:
        print(b)
    else:
        while(n>1):
            c=a+b
            a=b
            b=c
            c=+1
        return c


n = int(input("Enter a valid number:"))
print(fibonacci(n))
