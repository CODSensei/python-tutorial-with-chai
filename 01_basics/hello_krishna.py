print("Hello Krishna")

def chai(n):
    if (n == 1): 
        return 1;
    print(n)
    return chai(n - 1)

chai('x')    