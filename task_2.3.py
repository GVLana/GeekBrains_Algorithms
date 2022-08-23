
def vice_versa(num, check=0, res=''):
    if num == 0:
        print('The reverse number is: ')
        return res
    else:
        check = num % 10
        num = num // 10
        res = res + str(check)
        return vice_versa(num, check, res)

try:
    user_input = int(input('Enter a number: '))
    print(f'{vice_versa(user_input)}')
except ValueError:
    print('You enter a string not a number. Try again.')

