def ispalindrome(x):
    if not 0 < n < 10000:
        raise TypeError("not correct")
    if len(str(x))<4:
        x="0"*(4-len(str(x)))+str(x)
    if x[:2]==x[-2:][::-1]:
        print('число палиндром')
    else:
        print('число не палиндром')
    print(x)

n = int(input("Введите число: "))
ispalindrome(n)