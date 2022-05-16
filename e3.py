def is_n_prime(n, d = None):
    if(d is None):
        d = n - 1
    while(d >= 2):
        if(n % d == 0):
            print("this number is not prime")
            return False
        else:
            return is_n_prime(n, d - 1)
    else:
        print("this number is prime")
        return True

n = int(input("enter number: \n"))
is_n_prime(n)
