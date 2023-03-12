from statistic_functions import *


def zeroValue(x):
    if x == 0:
        print("For this case it`s not possible to choose 0")
        return True
    return False


def chooseValue():
    x = input("Input value:\t")
    x = float(x)
    return x


def checkPerc():
    x = input("Input percentage between 0 and 100 without %:\t")
    x = float(x)
    if 0 > x > 100:
        print("Your value", x, "is not supported")
        return None
    return x


def calculator():
    op = input("Choose level of functions\n"
               "A   for advanced\n"
               "B   for basic ones\n"
               "S   for statistic ones\n"
               "Q   to quit\n")
    if op == "B":
        op = input("Choose operation \n"
                   "+   for addition\n"
                   "-   for subtraction\n"
                   "*   for multiplication\n"
                   "/   for division\n"
                   "s   for square of number\n"
                   "r   for root of number\n"
                   "f   for factorial of number\n"
                   "si   for sine of the number\n"
                   "co   for cosine of the number\n"
                   "tg   for tangent of the number\n"
                   "ctg   for cotangent of the number\n"
                   "log   for logarithm when you don`t know base\n"
                   "log1   for logarithm when you know base\n"
                   "back   to go back\n")
        if op == "r":
            vr = chooseValue()
            vr = math.sqrt(vr)

        elif op == "s":
            vr = chooseValue()
            vr = str(vr)
            x = input("Choose power for your value " + vr + ":\t")
            x = float(x)
            vr = float(vr)
            vr = math.pow(vr, x)
        else:
            if op == "+":
                x = chooseValue()
                y = chooseValue()
                vr = x + y
            elif op == "*":
                x = chooseValue()
                y = chooseValue()
                vr = x * y
            elif op == "-":
                x = chooseValue()
                y = chooseValue()
                vr = x - y
            elif op == "/":
                x = chooseValue()
                y = chooseValue()
                if zeroValue(y):
                    return None
                vr = x / y
            elif op == "f":
                x = chooseValue()
                x = round(x)
                vr = math.factorial(x)
            elif op == "si":
                x = chooseValue()
                vr = math.sin(x)
            elif op == "co":
                x = chooseValue()
                vr = math.cos(x)
            elif op == "tg":
                x = chooseValue()
                vr = math.tan(x)
            elif op == "ctg":
                x = chooseValue()
                vr = math.cos(x) / math.sin(x)
            elif op == "log":
                print("Enter value of log:\t")
                x = chooseValue()
                vr = math.log(x)
            elif op == "log1":
                print("Enter value of log:\t")
                x = chooseValue()
                print("Enter value of log base\t")
                y = chooseValue()
                vr = math.log(x, y)
            elif op == "back":
                vr = calculator()
            else:
                print("Your value", op, "is not supported")
                return None
    elif op == "A":
        op = input("Choose operation\n"
                   "%   when you know two percentage values and return value for one of them\n"
                   "!%   when you know two return values and percentage for one of them\n"
                   "back   to go back\n")
        if op == "%":
            print("Enter percentage for which you know return value\n")
            x1 = checkPerc()
            if zeroValue(x1):
                return None
            print("Enter return value of percentage ", x1, "\n")
            y = chooseValue()
            print("Enter percentage for which you don`t know return value\n")
            x2 = checkPerc()
            vr = (x2 * y) / x1
        elif op == "!%":
            print("Enter percentage for which you know return value\n")
            x = checkPerc()
            print("Enter return value of percentage ", x, "\n")
            y1 = chooseValue()
            if zeroValue(y1):
                return None
            print("Enter return value for percentage you don`t know\n")
            y2 = chooseValue()
            vr = (x * y2) / y1
            if vr > 100:
                print("Percentages cannot be greater than 100%")
                return None
            vr = str(vr)
            vr = vr + "%"
        elif op == "back":
            vr = calculator()
        else:
            print("Your value", op, "is not supported")
            return None
    elif op == "S":
        op = input("Choose operation \n"
                   "m1   for MEAN\n"
                   "m2   for MEDIAN\n"
                   "m3   for MODE\n"
                   "cd   for calculating CONFIDENCE LEVEL value\n"
                   "pv   for VARIANCE OF POPULATION\n"
                   "psd   for STANDARD DEVIATION OF POPULATION\n"
                   "sv   for VARIANCE OF SAMPLE\n"
                   "ssd   for STANDARD DEVIATION OF SAMPLE\n"
                   "ci   for calculating CONFIDENCE INTERVAL\n"
                   "se   for calculating STANDARD ERROR\n"
                   "moe   for calculating MARGIN OF ERROR\n"
                   "q1   for calculating QUARTILE 25\n"
                   "q2   for calculating QUARTILE 50\n"
                   "q3   for calculating QUARTILE 75\n"
                   "iqr   for calculating IQR\n"
                   "back   to go back\n")
        if op == "m1":
            vr = mean1()
        elif op == "m2":
            vr = median()
        elif op == "m3":
            vr = mode()
        elif op == "cd":
            vr = cdCounter()
        elif op == "pv":
            vr = populationVariance()
        elif op == "psd":
            vr = populationStandardDeviation()
        elif op == "sv":
            vr = sampleVariance()
        elif op == "ssd":
            vr = sampleStandardDeviation()
        elif op == "ci":
            vr = confidenceInterval()
        elif op == "se":
            vr = StandardError()
        elif op == "moe":
            vr = marginOfError()
        elif op == "q1":
            vr = quartile25()
        elif op == "q2":
            vr = quartile50()
        elif op == "q3":
            vr = quartile75()
        elif op == "iqr":
            vr = IQR()
        elif op == "back":
            vr = calculator()
        else:
            print("Your value", op, "is not supported")
            return None
    elif op == "Q":
        print("Your value", op, "is not supported")
        return None
    else:
        vr = "You entered wrong value, please try again"
        return vr
    print("\n")
    return vr


c = 0
while c is not None:
    c = calculator()
    print(c, "\n\n")
