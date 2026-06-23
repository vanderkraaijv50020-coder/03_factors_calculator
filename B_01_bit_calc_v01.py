# generates headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# display instructions
def instruction():
    statement_generator("Instructions", "-")

    print('''
    To use this program simply enter an integer between 1 and 200.
    The program will show you the factors of your chosen integer

    It will also tell you 
    - is a prime number (ie: it has two factors)
    - is a perfect square

    To exit this program please type xxx
        ''')


# Display instructions if requested
want_instructions = input("press <enter> to read the instructions"
                          " or any key to continue")

if want_instructions == "":
    instruction()
print()
print("Program continues")
print()
# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        print()
        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)




# Main Routine Goes Here
while True:

    # list to hold the factors...
    factor_list = []

    to_factor = num_check("To factor: ")

    if to_factor == "xxx":
        break

    if to_factor == 1:
        print(f"One is special, it is UNITY (has only one factor)")
        continue


    for item in range(1, to_factor +1 ):

        num_students = item

        division = to_factor / num_students
        per_student = to_factor // num_students
        possible_factors = to_factor % item

        # Check to see if the number is a factor and add
        # it to the list of factors if it is.
        if possible_factors == 0:
            factor_list.append(item)

     # factor list
    print(factor_list)

    # Check if number is a prime number
    if len(factor_list) == 2:
        print(f"{to_factor} is a prime number")


    #Check if number is a perfect square
    elif len(factor_list) %2 == 1:
        print(f"{to_factor} is a perfect square")




