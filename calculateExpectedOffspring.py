def calculateExpectedOffspring(coupleList, offspringNum):
    prob_x = [1, 1, 1, 0.75, 0.5, 0]
    expected_x = 0
    for index in range(len(coupleList)):
        expected_x += coupleList[index] * offspringNum * prob_x[index]
    return expected_x
