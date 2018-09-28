def func(inStr):
    outStr = ''
    resStr = ''
    numStr = ''
    for i in inStr:
        if i == '*':
            outStr += i
        elif i.isdigit():
            numStr += i
        else:
            resStr += i
    print(outStr+numStr+resStr)
func('*a**b12**c8')
