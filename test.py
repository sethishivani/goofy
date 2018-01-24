def one(a,b):
    return a+b 
def two(a,b):
    return a-b
def three(a,b):
    return a*b
def numbers_to_months(argument,a,b):
    switcher = {
        1: one(a,b),
        2: two(a,b),
        3: three(a,b)
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    # Execute the function
    print func()
numbers_to_months(4,10,12)
