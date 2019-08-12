def divide(n):
    try:
        1/n
        chr(n)
    except (ArithmeticError, ZeroDivisionError):
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
