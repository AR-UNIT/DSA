import string

alphanumeric_chars = list(string.ascii_letters + string.digits)


def getHashp(password):
    power = len(password) - 1
    numerator = 0
    denominator = (10 ** 9) + 7
    for char in password:
        numerator += ord(char) * (131 ** power)
        power -= 1

    return numerator % denominator

def authorize(password, hashp_actual):
    if hashp_actual == str(getHashp(password)):
        return True
    for char in alphanumeric_chars:
        hashp_gen = getHashp(password + char)
        if hashp_actual == str(hashp_gen):
            return True

    return False


def authEvents(events):
    # Write your code here

    print(events)
    password = str()
    for event in events:

        if event[0] == "setPassword":
            password = event[1]
        elif event[0] == "authorize":
            if (authorize(password, event[1])):
                print("1")
            else:
                print("0")


# events = [["setPassword", "000A"], ["authorize", "108738450"], ["authorize", "108738449"], ["authorize", "244736787"]]
events = [["setPassword", "000A"], ["authorize", "244736787"]]


authEvents(events)