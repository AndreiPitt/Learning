def get_weather(temp):
    if temp > 30:
        return "hot"
    else:
        return "cold"


def add(x, y):
    return x + y


def divide(x, y):
    if y == 0:
        raise ValueError("You cant divide by zero.")
    else:
        return x / y
