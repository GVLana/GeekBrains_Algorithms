
def sequense_sum(n_count, n, i=0, n_sum=0):
    if i == n_count:
        print(f'The sequence length is {n_count}. The total sum is {n_sum}.')
        return " "
    else:
        i += 1
        n_sum += n
        return sequense_sum(n_count, n/2*-1, i, n_sum)

try:
    user_input = int(input('Enter the number - the length of the sequence: '))
    sequense_sum(user_input, 1)
except ValueError:
    print('You enter a string, not a number. Try again.')
