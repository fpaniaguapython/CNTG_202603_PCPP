a_list = ['First error', 'Second error']
try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10 but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f) # Inner exception (f): division by zero
        print('Outer exception (e):', e) # Outer exception (e): list index out of range
        print('Outer exception referenced:', f.__context__) # Outer exception referenced: list index out of range
        print('Is it the same object:', f.__context__ is e) # True