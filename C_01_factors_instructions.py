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
print("program continues")

