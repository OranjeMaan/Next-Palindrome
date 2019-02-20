#Created by Oranje Maan | 19 February 2018
#Program shall find the next palindrome from the given number


def Validate(string):
    #Checks if string is a whole number; returns true if it is or not
    bln = False
    #Check if the number is numeric
    #One could use string.isNumeric(), but that will return false for strings such as "2.5"; the program won't accept decimals, but it will tell not to use one if one is used
    try:
        float(string)
    except:
        print("Please enter a number and only a number.")
        return bln
    #Check if the number is an integer
    if float(string).is_integer():
        bln = True
    else:
        print("Please enter an integer.")
    return bln

def Clean(string):
    #Clean up string
    #Remove any spaces from inputed string
    string = string.replace(" ","")
    #Remove decimals points
    x = string.find(".")
    if x > -1:
        string = string[:x]
    return string

def main():
    strInput = input("Please enter a whole number.")
    while not Validate(strInput):
        strInput = input("Please enter a whole number.")
    #Commence to find next palindrome
    strInput = Clean(strInput)
    numInput = int(strInput)
    negative = False
    if numInput < 0:
        numInput = -numInput
        strInput = str(numInput)
        negative = True
    if numInput < 10:
        if negative:
            print("The next palindrome after " + strInput + " is -11.")
        else:
            print("The next palindrome after " + strInput + " is 11.")
        return
    #Get the first half of digits from the number
    firstHalf = strInput[0:(len(strInput)//2)]
    #Reverse the order of the first half
    firstHalfReverse = firstHalf[::-1]
    #Get latter half; determine if length is odd or even
    if len(strInput) % 2 == 0:
        latterHalf = strInput[(len(strInput)//2):len(strInput)]
        odd = False
    else:
        latterHalf = strInput[((len(strInput)//2) + 1):len(strInput)]
        odd = True
    #print(firstHalf)
    #print(latterHalf)
    #Check if the latter half is larger or smaller  or equal to the reverse first half
    if int(firstHalfReverse) > int(latterHalf):
        #Reverse first half is larger than the latter half
        #print("Larger")
        if odd:
            middle = strInput[(len(strInput)//2)]
            latterHalf = middle + firstHalfReverse
        else:
            latterHalf = firstHalfReverse
    else:
        #Reverse first half is not larger to the latter half; smaller or equal
        #print("Not larger")
        firstHalf = int(firstHalf)
        if odd:
            middle = int(strInput[(len(strInput)//2)]) + 1
            if middle > 9:
                middle = 0
                firstHalf += 1
        else:
            firstHalf += 1
        firstHalf = str(firstHalf)
        if odd:
            firstHalfReverse = str(middle) + firstHalf[::-1]
        else:
            firstHalfReverse = firstHalf[::-1]
        latterHalf = firstHalfReverse
    #Print next palindrome
    if negative:
        print("The next palindrome after -" + strInput + " is -" + firstHalf + latterHalf + ".")
    else:
        print("The next palindrome after " + strInput + " is " + firstHalf + latterHalf + ".")
    
main()
