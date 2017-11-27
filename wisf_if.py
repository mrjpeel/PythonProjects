answer = input('Are you a boy?')

if answer == 'yes':
    print('ok then good one!')
else:
    print('You what?')


answer = input('Are you a boy?\n')

if answer in ('yes', 'Yes', 'YES'):
    print('ok then good one!')
else:
    print('You what?')


#
answer = input('Are you a boy?\n')

if answer.lower() == 'yes':
    print('ok then good one!')
else:
    print('You what?')

#Yes ior No answer excepted
answer = input('Are you a boy?\n')

if answer.lower() == 'yes':
    print('ok then good one!')
elif answer.lower() == 'no':
    print('I assume then you were born a girl')
else:
    print('Please can you answer either yes or no')