def getinput():
    return int(input('Please enter a number: '))

def getsum(v1, v2):
    return v1 + v2


def printval(v1, v2, total):
    print(f'{v1} + {v2} = {total}')


def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
