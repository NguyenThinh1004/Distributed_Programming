import threading
import random
import time
from datetime import datetime
import math

A_SIZE = 150
A = [None] * A_SIZE

# Semaphore làm mutex cho A
array_mutex = threading.Semaphore(1)

# Semaphore báo có dữ liệu (được "giữ" luôn sau khi đã có >=1 phần tử)
data_available = threading.Semaphore(0)

# Đếm số phần tử đã ghi vào A (tối đa 150)
filled_count = 0
filled_lock = threading.Lock()

write_index = 0

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def is_perfect_square(x: int) -> bool:
    if x < 0:
        return False
    r = int(math.isqrt(x))
    return r * r == x

def producer(pid: int):
    global write_index, filled_count
    while True:
        val = random.randint(0, 10000)

        array_mutex.acquire()
        try:
            A[write_index] = val
            write_index = (write_index + 1) % A_SIZE

            # Cập nhật số phần tử đã có (tối đa 150)
            with filled_lock:
                if filled_count < A_SIZE:
                    filled_count += 1
                    # Khi lần đầu có dữ liệu, nhả semaphore
                    data_available.release()
        finally:
            array_mutex.release()

        print(f"P{pid}: {val} - {now_str()}")
        time.sleep(random.uniform(0.01, 0.1))

def consumer(cid: int):
    data_available.acquire()
    data_available.release()  # giữ semaphore luôn sẵn cho các lần sau

    while True:
        array_mutex.acquire()
        try:
            # Chọn ngẫu nhiên một vị trí đã được ghi
            with filled_lock:
                max_index = filled_count
            if max_index == 0:
                continue

            idx = random.randint(0, max_index - 1)
            val = A[idx]
        finally:
            array_mutex.release()

        if val is not None:
            result = "YES" if is_perfect_square(val) else "NO"
            print(f"C{cid}: {val} - {result} - {now_str()}")

        time.sleep(random.uniform(0.01, 0.1))

def main():
    producers = [threading.Thread(target=producer, args=(i+1,), daemon=True) for i in range(5)]
    consumers = [threading.Thread(target=consumer, args=(i+1,), daemon=True) for i in range(5)]

    for t in producers + consumers:
        t.start()

    # Chạy vô hạn
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()