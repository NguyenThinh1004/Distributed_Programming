import random
import threading
import time
from datetime import datetime

N = 150
K = 3
H = 3

data_lock = threading.Lock()
has_item = threading.Semaphore(0)

A = []

def now_str():
	return datetime.now().strftime("%H:%M:%S.%f")

def is_prime(n):
	if n < 2:
		return False
	if n % 2 == 0:
		return n == 2
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True

def producer(id):
	while True:
		time.sleep(random.uniform(0.2, 1.2))
		value = random.randint(1, 10_000)
		with data_lock:
			A.append(value)
		has_item.release()
		print(f"P{id}: {value} - {now_str()}")

def consumer(id):
	while True:
		has_item.acquire()
		with data_lock:
			value = random.choice(A)
		result = "prime" if is_prime(value) else "not prime"
		print(f"C{id}: {value} - {result} - {now_str()}")
		time.sleep(random.uniform(0.2, 1.0))

def main():
	threads = []

	for i in range(K):
		t = threading.Thread(target=producer, args=(i + 1,), daemon=True)
		threads.append(t)
		t.start()

	for i in range(H):
		t = threading.Thread(target=consumer, args=(i + 1,), daemon=True)
		threads.append(t)
		t.start()

	while True:
		time.sleep(1.0)
		
    # for t in threads:
    #     t.join()

if __name__ == "__main__":
	main()
