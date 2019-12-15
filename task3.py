def reverse_digit(num):
    if num<10:
        return num
    else:
        return  int((str(num%10)+str(reverse_digit(num//10))))
print(reverse_digit(1478))