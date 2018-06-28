try:
    try:
        l = [1, 2, 3]
        print(l[3])
    except:
        print("it has index error")
    #import moth
    x = int(input('Enter First Number: '))
    y = int(input('Enter Second Number: '))
    print(x/y)
    import moth
except ( ValueError,ImportError):
    print('Wrong input!')