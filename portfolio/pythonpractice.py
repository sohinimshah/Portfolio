#Write a program that computes the sum of the first 20 positive integers

#integers = [1, 2, 3, 4, 5, 6, 7, 8, ,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def sumInts():
    sum = 0
    for i in range(0, 20):
        sum = sum + i
    return sum



def main():
    sum = sumInts()
    print(sum)
main()
