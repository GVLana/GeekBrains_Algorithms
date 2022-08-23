
def ascii_table(n=32, m=127, size=1):
    if n > m:
        return True
    print(n, chr(n), sep=' - ', end=' ')
    if size % 10 == 0:
        print('\n')
    n += 1
    size += 1
    ascii_table(n, m, size)


ascii_table()

