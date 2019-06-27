from numpy import arange
import matplotlib.pyplot as plot
import math

def F2C(nDegreesF):
    # my code
    nDegreesC = (nDegreesF - 32) * (5.0/9.0)
    return nDegreesC
def C2F(nDegreesC):
    nDegreesF = (1.8 * nDegreesC) + 32
    return nDegreesF
userInputF = float(input("enter Fahrenheit: "))
newTempF = F2C(userInputF)

userInputC = float(input("Enter Celsius: "))
newTempC = C2F(userInputC)

print(" The temperature in Celsius is: ", newTempC)
print("The temperature in Fahrenheit is: ", newTempF)



x_axis = list(range(0, 100))
y_axis = list(range(0, 100))


plot.scatter(newTempC, 1)
plot.show()