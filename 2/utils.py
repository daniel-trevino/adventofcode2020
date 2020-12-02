from constants import INPUT_FILE_NAME


def getInputValues():
    inputValues = open(INPUT_FILE_NAME, 'r')
    inputArray = []
    for value in inputValues:
        valueAsJson = convertLineToJson(value)
        inputArray.append(valueAsJson)
    inputValues.close()
    return inputArray


def convertLineToJson(inputValue):
    values = inputValue.split()
    splitMinMax = values[0].split("-")
    return {
        "min": int(splitMinMax[0]),
        "max": int(splitMinMax[1]),
        "symbol": values[1].replace(':', ''),
        "password": values[2]
    }
