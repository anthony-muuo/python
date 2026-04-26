# prime number checker!

def prime_checker(number):
    if (number <= 1):
       print("It's not a prime number")
       return
    
    is_prime = True
    for i in range(2, number-1):
        if number % i ==0:
            is_prime= False
            break
        
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")
                    
        

number = int(input("Prime number checker. Check this number? "))

prime_checker(number)