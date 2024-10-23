"""
getRegularExpression: Function that reads regular expression and break them down into minimal parts
regularExpression: User Input containing regular expression
return: Array conintainig minimal parts of regular expression
"""
def getRegularExpression(regularExpression):

    expression = list()
    symbol = ""

    openSymbol = 0
    openSet = 0

    for i in regularExpression:

        # Validate the start of the set
        if (i == "("):
            openSet += 1
            # Validates if close the alphabet
            if (openSet == 2):
                raise ValueError(r"Recordar la sintax para ingresar un nuevo conjunto, \n Validar que cada conjunto este encerrado entre ( )")
            expression.append(i)
        # Validate the end of the set
        elif (i == ")"):
            if (openSet == 0):
                raise ValueError(r"Recordar la sintax para ingresar un nuevo simbolo, \n Validar que cada simbolo este encerrado entre { }")
            openSet -= 1
            expression.append(i)

        # Validate star lock
        elif (i == "*"):
            expression.append(i)

        # Validate positive lock
        elif (i == "*"):
            expression.append(i)

        # Validate union
        elif (i == ","):
            expression.append(i)

        # Validates the beginning of the alphabet     
        elif (i == "{"):
            openSymbol += 1
            # Validates if close the alphabet
            if (openSymbol == 2):
                raise ValueError(r"Recordar la sintax para ingresar un nuevo simbolo, \n Validar que cada simbolo este encerrado entre { }")
            symbol = ""
        # Validates the end of the alphabet  
        elif (i == "}"):
            # Validates if open the alphabet
            if (openSymbol == 0):
                raise ValueError(r"Recordar la sintax para ingresar un nuevo simbolo, \n Validar que cada simbolo este encerrado entre { }")
            openSymbol -= 1
            expression.append(symbol)
        else:
            symbol += i
    
    return expression

def validateChain(chain, expression):

    flag = True

    for eR in expression:
        for symbol in chain:
            if (symbol != eR):
                flag = False
                exit

expressions = getRegularExpression(r"({a}{b}{ab})*{c}({a},{b})")

for i in expressions:
    print(i)

        
