import multiprocessing as mp
import numpy as np

def sumit(producer_q, consumer_q):
    while True:
        x = producer_q.get()
        if x == 'CLOSE':
            break
        consumer_q.put(int(x) * 2)
        print(x)
        
    return 0

def main():
    
    producer_q = mp.Queue()
    consumer_q = mp.Queue()
        
    workers = [mp.Process(target=sumit, args=(producer_q,consumer_q,)) for i in range(2)]
    for w in workers:
        w.start()
        
    # submit job to queue
    for i in range(6):
        producer_q.put(i)
    
    # close workers
    for i in range(2):
        producer_q.put('CLOSE')
        
    # consume all processed info
    vals = []
    for i in range(6):
        val = consumer_q.get()
        vals.append(val)
    
    # block all processing till workers terminate
    for w in workers:
        w.join()
        
    print(f'vals: {vals}')
    
    return 0

if __name__ == '__main__':
    main()