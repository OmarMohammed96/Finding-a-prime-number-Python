"""Finding a prime number in a given range."""
# Prime number is natural number greater than 1, that has no positive divisors other than 1 and itself.

print('This program helps you find the prime number in any selected range.')

# the user need to inter the range.
lower = int(input('Enter the lower interval: '))
upper = int(input('inter the upper interval: '))

for number in range(lower,upper+1):
    if number > 1:                      # Prime number should be grater than 1.
        for x in range(2,number):       # The range start from 2 because prime number isgreater than 1.
            if number % x == 0:         # Check if the number in the range is divisibal by the all number smaller than it.
                break 
        else:
            print(number)
