# This code should print out apples, bananas, tofu, and cats.

spam = ["apples", "bananas", "tofu", "cats"]

def lister(passedList):

    listLength = len(passedList) #calculates length of the list
    lessOne = listLength - 1 #subtracts one so we know where to add the "and"


    for i in (passedList):
         print(str(i) + ", ",  end="")


    #print(listLength)
    #print(lessOne)



lister(spam)

