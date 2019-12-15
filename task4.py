def encode2(num):
    if num//2==0:
        return num
    else:
        return  str(num%2)+str(encode2(num//2))
print(encode2(145))