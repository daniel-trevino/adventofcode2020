from constants import INPUT_FILE_NAME, STEPS_RIGHT, STEPS_DOWN, TREE


def getInputValuesAsMatrix():
    inputValues = open(INPUT_FILE_NAME, 'r')
    inputX = []
    for row in inputValues:
        normalizeColumn = row.replace('\n', '')
        inputY = []
        for track in normalizeColumn:
            inputY.append(track)
        inputX.append(inputY)
    inputValues.close()
    return inputX


def rideTheToboggan():
    trajectoryMap = getInputValuesAsMatrix()
    slopeTrack = []
    positionX = 0
    positionY = 0
    hasReachedEnd = False
    numberOfTrees = 0
    for row in range(len(trajectoryMap)-1):
        positionX += STEPS_RIGHT
        positionY += STEPS_DOWN
        if (hasReachedEnd):
            break
        # Gets the limit to the right and down of the map
        lastCoordinateX = len(trajectoryMap[row])-1
        lastCoordinateY = len(trajectoryMap)-1

        if (positionX > lastCoordinateX):
            positionX = resetPosition(positionX, lastCoordinateX)
        if (positionY > lastCoordinateY):
            hasReachedEnd = True  # We don't want to continue iterating since we have reached the end
            positionY = resetPosition(positionY, lastCoordinateY)

        mapPosition = trajectoryMap[positionY][positionX]
        if (mapPosition == TREE):
            numberOfTrees += 1

        # Save the trajectory on a list
        slopeTrack.append(trajectoryMap[positionY][positionX])
        print(slopeTrack)
    print(slopeTrack)
    return numberOfTrees


def resetPosition(position, lastCoordinate):
    difference = position - lastCoordinate
    balancetoIndexZero = 1
    return difference - balancetoIndexZero
