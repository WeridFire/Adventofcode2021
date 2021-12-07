def getTheInput(path):
    file = open(path)
    input = file.readlines()
    for i in range(len(input)):
        input[i] = input[i].removesuffix("\n")
    return input

def mainone(input):
    n = 0
    for i in range(len(input)):
        if int(input[i]) > int(input[i-1]) and i != 0:
            n = n + 1
    return n

def maintwo(input):
    output = []
    for i in range(len(input)):
        if i < len(input) - 2:
            a = int(input[i]) + int(input[i+1]) + int(input[i+2])
            output.append(a)

        n = mainone(output)
    return n


print(str(mainone(getTheInput('input'))))
print(str(maintwo(getTheInput('input'))))

