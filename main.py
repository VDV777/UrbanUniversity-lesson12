from random import random, randint


def getNumberPass(minNumber: int, maxNumber: int) -> str:

    variant = randint(minNumber, maxNumber)
    print(f'variant: {variant}')
    password = ''

    for firstNum in range(1, variant):

        for secondNum in range(firstNum + 1, variant):

            if (firstNum + secondNum) % variant == 0:

                password += f'{firstNum} + {secondNum} '

    return password


print(getNumberPass(3, 20))





