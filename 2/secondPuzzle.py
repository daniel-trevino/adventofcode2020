from utils import getInputValues


def findValidPasswords():
    inputValues = getInputValues()
    count = 0
    for passwordObject in inputValues:
        if isValidPassword(passwordObject) is True:
            count += 1
            print(passwordObject)
    return count


def isValidPassword(passwordObject):
    passwordAsList = list(passwordObject['password'])
    if (passwordAsList[passwordObject['min'] - 1] == passwordObject['symbol'] and passwordAsList[passwordObject['max'] - 1] == passwordObject['symbol']):
        return False

    return passwordAsList[passwordObject['min'] - 1] == passwordObject['symbol'] or passwordAsList[passwordObject['max'] - 1] == passwordObject['symbol']
