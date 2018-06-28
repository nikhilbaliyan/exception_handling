count = int(input('Enter your age'))
if(count<18):
    try:
        print(' WARNING! your age is less than 18')
        raise AgeTooSmallError('good bye')
    except:
        print('plz enter the valid age')
else:
    print("thank you")
