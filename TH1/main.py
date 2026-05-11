import random
import threading
from datetime import datetime
import math

N = 10
THREADS = 3
THREAD_SIZE = N // THREADS

A = [random.randint(1, 1000) for _ in range(N)]
A.append(1000)
print("Mảng A:", A)

results = [None] * THREADS

def find_max(thread_id, start, end):
    local_max = None
    for i in range(start, end):
        val = A[i]
        if local_max is None or val > local_max:
            local_max = val
            timestamp = datetime.now().strftime("%H:%M:%S.%f")
            # print(f"T{thread_id}: {local_max} : {timestamp}")
    results[thread_id - 1] = local_max
    print(f"T{thread_id}: {local_max} : {timestamp}")

threads = []
for i in range(THREADS):
    start = i * THREAD_SIZE
    if i == THREADS - 1:
        end = N+1
    else:
        end = start + THREAD_SIZE
    t = threading.Thread(target=find_max, args=(i + 1, start, end))
    threads.append(t)
    t.start()

for t in threads:
    t.join() # đảm bảo luồng chính đợi tất cả luồng hoàn thành

final_max = max(results)
print(f"Kết quả cuối cùng (max toàn mảng): {final_max}")