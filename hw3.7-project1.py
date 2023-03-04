def get_scores():
    # Create an empty list.
    test_scores = []

    # Create a variable to control the loop.
    again = 'y'

    # Get the scores from the user and add them to the list.
    while again == 'y':
        # Get a score and add it to the list.
        value = float(input('Enter a test score: '))
        test_scores.append(value)

        # Want to do this again?
        print('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()

    # Return the list.
    return test_scores

def get_total(value_list):
    # Create a variable to use as an accumulator.
    total = 0.0

    # Calculate the total of the list elements.
    for num in value_list:
        total += num

    # Return the total.
    return total

def main():
    # Get the test scores from the user.
    scores = get_scores()

    # Calculate the total of the test scores.
    total = get_total(scores)

    # Display the total of the test scores.
    print('The total of the test scores is', total)

# Call the main function.
if __name__ == '__main__':
    main()
