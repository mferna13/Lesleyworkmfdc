secret_number = 87
n = input('Guess the secret number between 1 and 100 ')
n = int(n) # convert user input into an integer
if n == secret_number:
 print('You got it!')
else:
 # not equal to secret_number so check if lower or higher
 if n > secret_number:
    print('Your guess was too high')
 else:
     print('Your guess was too low')
     print('Thanks for playing') # this is done at end in all cases