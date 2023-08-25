import threading
import queue
import time
import sys


shared_queue = queue.Queue()


def producer(producer_id, items):
    for item in items:
        print(f"Producer {producer_id}: Producing item {item}")
        shared_queue.put(item)
        time.sleep(1)


def consumer(consumer_id):
    while True:
        try:
            item = shared_queue.get(timeout=2)
            print(f"Consumer {consumer_id}: Consuming item {item}")
            shared_queue.task_done()
        except queue.Empty:
            break

def main():
    num_producers = int(input("Enter the number of producers: "))
    num_consumers = int(input("Enter the number of consumers: "))


    producer_threads = []
    for i in range(num_producers):
        items = [f"item_{i}_{j}" for j in range(3)]  
        producer_threads.append(threading.Thread(target=producer, args=(i, items)))

    
    consumer_threads = []
    for i in range(num_consumers):
        consumer_threads.append(threading.Thread(target=consumer, args=(i,)))

   
    for thread in producer_threads + consumer_threads:
        thread.start()

    
    for thread in producer_threads + consumer_threads:
        thread.join()

    print("All producers and consumers have finished.")

if __name__ == "__main__":
    main()
