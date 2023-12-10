spam = ["apples", "bananas", "tofu", "cats"]

def lister(passedList):
    listLength = len(passedList)
    for items in (passedList):
        print(str(items) + ", ")
    print(listLength)



lister(spam)

