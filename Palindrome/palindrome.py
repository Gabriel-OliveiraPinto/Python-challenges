import re

def main():
    word = input("Type the word: ")
    
    isPalindrome = checkPalindrome(word)

    if(isPalindrome):
        print(word + " is a palindrome")
    else:
        print(word + " is not a palindrome")



def checkPalindrome(word):
    #Use regex to get a to z only, excluding any kind of pontuation
    word = "".join(re.findall(r'[a-z]+', word.casefold()))
    print(word)
    reverse = word[::-1]
    if(word == reverse) : 
        return True
    else:
        return False



if __name__ == "__main__":
    main()
