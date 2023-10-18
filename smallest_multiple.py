"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def Problem005(n):
	m = 0
	Found = False
	while not Found:
		m += n
		for i in range(1, n):
			Found = (m % i == 0)
			if not Found:
				break
	return m



def time_function(f, *args):
    import time
    t0 = time.time()
    v = f(*args)
    t1 = time.time()
    t = t1 - t0
    print(f"{v} in {t:.2e} seconds from {f.__name__}{args}")
    return t1 - t0

# # time Problem005() for benchmarking
time_function(Problem005, 20)