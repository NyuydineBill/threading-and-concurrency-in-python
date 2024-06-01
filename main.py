import threading
import time

def func(lock):
    print('Thread started:', threading.current_thread().name)
    with lock:
        print('Running:', threading.current_thread().name)
        time.sleep(1)
        print('Finished:', threading.current_thread().name)

lock = threading.Lock()  # Create a lock object for synchronization

# Create and start multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=func, args=(lock,))
    threads.append(t)
    t.start()

time.sleep(0.5)  # Delay to allow threads to start

print('Active Threads:', threading.active_count())

# Wait for all threads to finish using join()
for t in threads:
    t.join()

print('All threads finished')