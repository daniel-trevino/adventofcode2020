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
    count = passwordObject['password'].count(passwordObject['symbol'])
    return count >= passwordObject['min'] and count <= passwordObject['max']
