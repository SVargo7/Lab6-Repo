# Sydney Vargo & Isabella Armendariz
# October 27, 2023

def main():
    # make menu
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(num):
    # create lists
    numsList = []
    answerList = []

    # add digits in number to list
    for char in num:
        numsList.append(char)

    # make digits integers
    numsList = [int(char) for char in numsList]

    # increase by 3
    for digit in numsList:
        if digit == 7:
            newDigit = 0
        elif digit == 8:
            newDigit = 1
        elif digit == 9:
            newDigit = 2
        else:
            newDigit = digit + 3

        # add them to an answer list
        answerList.append(newDigit)

    # make it a string again
    answer = ""
    for value in answerList:
        answer += str(value)

    # return string
    return answer