def even_odd(num, e_count=0, odd_count=0):
    if num == 0:
        print("Количество четных и нечетных цифр в числе равно: ")
        return e_count, odd_count
    else:
        check = num % 10
        num = num // 10
        if check % 2 == 0:
            e_count += 1
        else:
            odd_count += 1
        return even_odd(num, e_count, odd_count)


try:
    user_input = int(input("Enter a natural number: "))
    print(f'{even_odd(user_input)}')
except ValueError:
    print('You enter a string not a number. Try again.')

