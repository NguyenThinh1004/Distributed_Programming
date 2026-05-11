import random
import threading
from datetime import datetime
import math

N = 150
THREADS = 5
THREAD_SIZE = N // THREADS

A = [random.randint(1, 1000) for _ in range(N)]

results = [None] * THREADS

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes(thread_id, start, end):
    count = 0
    for i in range(start, end):
        if is_prime(A[i]):
            count += 1
            timestamp = datetime.now().strftime("%H:%M:%S.%f")
            print(f"T{thread_id}: {A[i]} : {timestamp}")
    results[thread_id - 1] = count

threads = []
for i in range(THREADS):
    start = i * THREAD_SIZE
    if i == THREADS - 1:
        end = N
    else:
        end = start + THREAD_SIZE
    t = threading.Thread(target=count_primes, args=(i + 1, start, end))
    threads.append(t)
    t.start()

for t in threads:
    t.join() # đảm bảo luồng chính đợi tất cả luồng hoàn thành

total_primes = sum(results)
print(f"Số nguyên tố: {total_primes}")