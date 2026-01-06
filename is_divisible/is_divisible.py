# This function checks if the first number can be divided by all other numbers provided.
    # It returns True if divisible by all, False otherwise.
    # It also handles division by zero and prints which numbers are not divisible.
def is_divisible(*args):
    if len(args)<2:
        return "Please provide at least tow numbers"
    first =args[0]

    for i in args[1:]:
        if i == 0:
            return "Division bty Zero"
        if first % i !=0:
            print(f"{first} is not Division by {i}")
            return False
    return True