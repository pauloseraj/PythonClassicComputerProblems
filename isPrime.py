def isPrime(number) -> bool:

    if(number<2):
            return False;
    for i in range(2,number):
        if(number%i ==0):
                return False;

    return True;

def main():
    print(isPrime(10));


main();
