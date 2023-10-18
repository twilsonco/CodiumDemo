from math import sqrt

def Problem007(num):
    def IsPrime(n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0:
            return False
        m = int(sqrt(n) + 1)
        if m % 2 == 0:
            m += 1
        for i in range(3, m, 2):
            if n % i == 0:
                return False
        return True
    i = 1
    count = 1  # 2 is the first prime
    while count < num:
        i += 2
        if IsPrime(i):
            count += 1
    return i


def time_function(f, *args):
    import time
    t0 = time.time()
    v = f(*args)
    t1 = time.time()
    t = t1 - t0
    print(f"{v} in {t:.2e} seconds from {f.__name__}{args}")
    return t1 - t0

time_function(Problem007, 100001)