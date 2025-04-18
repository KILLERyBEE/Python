
def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            is_prime = 0
            break
        is_prime = 1
    return is_prime

n = int(input("Enter A Number : "))
if(is_prime(n)):
    print("Num is Prime:")
else:
    print("Not prime")
