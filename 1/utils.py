from constants import SUM_OF_ENTRIES, INPUT_FILE_NAME


def getInputArray():
    inputValues = open(INPUT_FILE_NAME, 'r')
    inputArray = []
    for value in inputValues:
        inputNumber = int(value)
        inputArray.append(inputNumber)
    inputValues.close()
    return inputArray


def getResultOfTwoEntries(inputArray):
    for i in range(len(inputArray)):
        for y in range(len(inputArray)-i):
            indexSecondNumber = y + i
            if (inputArray[i] + inputArray[indexSecondNumber] == SUM_OF_ENTRIES):
                firstNumber = inputArray[i]
                secondNumber = inputArray[indexSecondNumber]
                result = firstNumber * secondNumber
                print(
                    'Two entries: {0} * {1} = {2}').format(firstNumber, secondNumber, result)
                return result


def getResultOfThreeEntries(inputArray):
    for i in range(len(inputArray)):
        for x in range(len(inputArray)-i):
            for y in range(len(inputArray)-x):
                indexSecondNumber = x + i
                indexThirdNumber = y + x
                if (inputArray[i] + inputArray[indexSecondNumber] + inputArray[indexThirdNumber] == SUM_OF_ENTRIES):
                    firstNumber = inputArray[i]
                    secondNumber = inputArray[indexSecondNumber]
                    thirdNumber = inputArray[indexThirdNumber]
                    result = firstNumber * secondNumber * thirdNumber
                    print('Three entries: {0} * {1} * {2} = {3}').format(
                        firstNumber, secondNumber, thirdNumber, result)
                    return result
