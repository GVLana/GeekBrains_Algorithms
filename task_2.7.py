
def check_equation(n):
    if n == 1:
        return n
    else:
        return check_equation(n-1) + n

#
# try:
#     user_input = input('Enter a natural number: ')
#     if user_input.isdigit() and user_input != '0':
#         num = int(user_input)
#         if check_equation(num) == num * (num + 1) / 2:
#             print('The equality is true.')
#         else:
#             print('The equality is false.')
#     elif user_input == '0':
#         print(f'{user_input} is not valid option. Try again.')
#     else:
#         print('You enter a string, not a number. Try again.')
# except ValueError:
#     print('Something went wrong.')


try:
    user_input = int(input('Enter a natural number, starts from 1: '))
    if check_equation(user_input) == user_input * (user_input + 1) / 2:
        print('The equality is true.')
    else:
        print('The equality is false.')
except ValueError:
    print('You enter a string, not a number. Try again.')

