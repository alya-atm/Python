def prime_factors(num, i=2):
    if num < i:
        return []
    if num % i == 0:
        return [i] + prime_factors(num / i, i)
    else:
        return prime_factors(num, i + 1)

print(prime_factors(18))