# Arithmatic Operators
countOfMongos, countOfApples = 10, 3

# Addition
answer = countOfMongos + countOfApples
print("Arithmatic Operators : ")
print(f"Addition : {countOfMongos} + {countOfApples} = {answer}")

# subtraction
answer = countOfMongos - countOfApples
print(f"subtraction : {countOfMongos} - {countOfApples} = {answer}")

# multiplication
answer = countOfMongos * countOfApples
print(f"multiplication : {countOfMongos} * {countOfApples} = {answer}")

# division
answer = countOfMongos / countOfApples
print(f"division : {countOfMongos} / {countOfApples} = {answer}")

# modulus
answer = countOfMongos % countOfApples
print(f"modulus : {countOfMongos} % {countOfApples} = {answer}")

# exponention
answer = countOfMongos ** countOfApples
print(f"exponention : {countOfMongos} ** {countOfApples} = {answer}")

# Floor Division
answer = countOfMongos // countOfApples
print(f"Floor Division : {countOfMongos} // {countOfApples} = {answer}")

def demonstrate_relational_operators():
    # Relational Operators
    countOfMongos, countOfApples = 10,3

    # Equal to
    answer = countOfMongos == countOfApples 
    print("\n Relational Operators : ")
    print(f"Equal to : {countOfMongos} == {countOfApples} -> {answer}")

    # Not Equal to
    answer = countOfMongos != countOfApples
    print(f"Not Equal to : {countOfMongos} != {countOfApples} -> {answer}")

    # Greater Than
    answer = countOfMongos > countOfApples
    print(f"Greater Than : {countOfMongos} > {countOfApples} -> {answer} ")

    # Less Than
    answer = countOfMongos < countOfApples
    print(f"Less Than : {countOfMongos} < {countOfApples} -> {answer} ")

    # Greater Than or equal to 
    answer = countOfMongos >= countOfApples
    print(f"Greater Than or equal to  : {countOfMongos} >= {countOfApples} -> {answer} ")

    # less Than or equal to 
    answer = countOfMongos <= countOfApples
    print(f"Less Than or equal to  : {countOfMongos} <= {countOfApples} -> {answer} ")

def demonstarte_logical_operators():
    # Logical Operators
    isReady, isGood = True , False

    # AND
    answer = isReady and isGood
    print("\nLogical Operators : ")
    print(f"AND: {isReady} and {isGood} -> {answer}")

    # OR
    answer = isReady or isGood
    print(f"OR: {isReady} or {isGood} -> {answer}")

    # OR
    answer = not isReady
    print(f"NOT : {isReady} -> {answer}")

def demonstarte_bitwise_operators():
    redTeamScore, whiteTeamScore = 16, 2

    # AND
    answer = redTeamScore & whiteTeamScore
    print("\n Bitwise Operators: ")
    print(f"AND : {redTeamScore} & {whiteTeamScore} -> {answer}")

    
    # OR
    answer = redTeamScore | whiteTeamScore
    print(f"OR : {redTeamScore} | {whiteTeamScore} -> {answer}")

    # XOR
    answer = redTeamScore ^ whiteTeamScore 
    print(f"XOR : {redTeamScore} ^ {whiteTeamScore} -> {answer}")

    # NOT
    answer = ~whiteTeamScore # n = -(n+1)
    print(f"NOT : ~{whiteTeamScore}  -> {answer}")

    # Left Shift
    answer = redTeamScore << whiteTeamScore
    print(f"Left Shift : {redTeamScore} << {whiteTeamScore}  -> {answer}")
    
    # Right Shift
    answer = redTeamScore >> whiteTeamScore
    print(f"Right Shift : {redTeamScore} >> {whiteTeamScore} -> {answer}")

def demonstarte_assignment_operator():
    totalScore = 3

    # Add and Assign
    totalScore = totalScore + 2
    answer = totalScore
    print(f"Add and assign : totalScore += 2 -> {answer}")

    # Subtract and Assign
    totalScore = totalScore - 2
    answer = totalScore
    print(f"Subtract and assign : totalScore -= 2 -> {answer}")

    # Multiply and Assign
    totalScore = totalScore * 2
    answer = totalScore
    print(f"Multiply and Assign : totalScore *= 2 -> {answer}")

    # division and assign
    totalScore = totalScore / 2
    answer = totalScore
    print(f"division and assign : totalScore /= 2 -> {answer}")

    # modulus and assign
    totalScore = totalScore % 2
    answer = totalScore
    print(f"modulus and assign : totalScore %= 2 -> {answer}")

    # Floor Divide and assign
    totalScore = totalScore // 2
    answer = totalScore
    print(f"Floor Divide and assign : totalScore //= 2 -> {answer}")

    # Exponent and assign
    totalScore = totalScore ** 2
    answer = totalScore
    print(f"Exponent and assign : totalScore **= 2 -> {answer}")

def demonstrate_operators():
        demonstrate_relational_operators()
        demonstarte_logical_operators()
        demonstarte_bitwise_operators()
        demonstarte_assignment_operator()

demonstrate_operators()