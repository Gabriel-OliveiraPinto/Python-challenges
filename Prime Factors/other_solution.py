def otherSolution():

    #Quite simple, get dividing the number, starting with 2
    #Keep dividing, only if the dividend is 0, avoiding non-prime factors
    number = int(input('Type your number: '))
    list = []
    
    for i in range(2 , number):

        while(number % i == 0):

            list.append(i)
            number /= i

        i += 1

    print(list)
        









