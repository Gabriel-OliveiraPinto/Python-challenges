thisList = []

def mySolution():
    #Take the input from the user
    number = int(input("Type a number: "))
    #Using the input, makes a list of prime numbers until reaching the input number
    makePrimeList(number)
    #Then, use the created list to get the PrimeFactors
    listPrimeFactors = getPrimeFactors(number)
    print(listPrimeFactors)


def makePrimeList(number):
    for num in range(2 , number + 1):

        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            thisList.append(num)


def getPrimeFactors(number):
    num = number
    list = []
    for i in thisList:
        while(num % i == 0):
            list.append(i)
            num /= i
    return list   



