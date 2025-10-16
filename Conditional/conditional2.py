# Definition
def getClassForPercentage(percentage: float) -> str:
    if(percentage >= 75):
        return "Distinction"
    elif (percentage >= 60):
        return "First Class"
    elif (percentage >= 50):
        return "Second Class"
    elif(percentage >= 35):
        return "Third Class"
    else:
        return "Failed"
    
percentage = 99
result = getClassForPercentage(percentage)
print(result)