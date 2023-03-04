#Written by Shiven Desai
#This program displays numbers in different ways
def main():
    numbers = []
    for i in range(20):
        num = float(input('Enter a number: '))
        numbers.append(num)
    lowest = min(numbers)
    print('The lowest number is:', lowest)

    highest = max(numbers)
    print('The highest number is', highest)

    total = sum(numbers)
    print('The total of the numbers is:', total)

    average = total / len(numbers)
    print('The average of the numbers is', average)

main()