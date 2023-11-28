def prime_number(n):
    for i in range(2, n):
        if not n % i == 0:
            return False
    return True
