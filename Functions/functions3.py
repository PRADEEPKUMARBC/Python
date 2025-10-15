# Function definition 
def IamFirst() -> None:
    print("I am first function")
    IamFirst()


def IamSecond() -> None:
    print("I am second function")
    IamSecond()


IamFirst()
IamSecond()