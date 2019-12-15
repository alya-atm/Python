def digits_sum(num):
    if num<10:
        return num
    return num%10+digits_sum(num//10)
def digital_root(num):
    return num if num < 10 else digital_root(digits_sum(num))
print(digital_root(447))