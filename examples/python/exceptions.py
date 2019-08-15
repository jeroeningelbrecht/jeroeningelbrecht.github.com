def divide(n):
    try:
        1/n
        chr(n)
    except (ArithmeticError, ZeroDivisionError) as e:
        print(e)
        print('oops, not a correct mathematical operation')
    except ValueError:
        print('wrong value José: ', n)
    else:
        print('else is only executed in case no exception was caught')
    finally:
        print('finally is always executed')


divide(0)
print('------------------')
divide(-1)
print('------------------')
divide(2)

# -------------------------------------------------------------------- #


def as_error(text):
    try:
        int(text)
    except ValueError as error:
        print('an error occurred')
        print(error)


as_error('hello')

# -------------------------------------------------------------------- #
