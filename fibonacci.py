def get_fib_list_length():

    return 15


def generate_fib(num):

    result = []

    # once for each number from 0 up to `num`.

    for n in range(num):
        if n == 0:
            result.append(0)

        elif n == 1:
            result.append(1)

        else:
            value = result[n - 2] + result[n - 1]
            result.append(value)


    return result


def display_fibs(fibs):
    for fib in fibs:
        print(fib)


def main():
    fib_limit = get_fib_list_length()
    fibs = generate_fib(fib_limit)
    display_fibs(fibs)


main()
