import math
segment = 20
frequency = 2
q = 1 * (1.602176634 * 10**-19)  # q = 1 * e
mass = 6.941
referencePhase = 3.14 / 4
maximumVoltage = 200
partialFraction = 1 / frequency
denominator = segment * q * maximumVoltage * math.sin(referencePhase)
numerator = 2 * mass
squareRoot = math.sqrt(denominator / numerator)

finalResult = partialFraction * squareRoot
print("The length result for this question is    ", finalResult)


# SOLVING IT USING PYTHON FUNCTION ;

def medicalApp():
    print("Test cases >>>>>>>>>>>>>>>>>>>>>>")
    frequency = float(input('Enter the value of Frequency '))
    segment = float(input('Enter the value of segment '))
    mass = float(input('Enter the value of mass '))
    maximumVoltage = float(input('Enter the value of maximumVoltage '))
    q = 1 * (1.602176634 * 10**-19)  # q = 1 * e
    referencePhase = 3.14 / 4
    partialFraction = 1 / frequency
    denominator = segment * q * maximumVoltage * math.sin(referencePhase)
    numerator = 2 * mass
    squareRoot = math.sqrt(denominator / numerator)
    finalResult = partialFraction * squareRoot
    print("the length is ", finalResult)
    return finalResult


medicalApp()
