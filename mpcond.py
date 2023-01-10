import multiprocessing as mp
from time import sleep
import numpy as np

def worker(q):
    g = q.get()
    print(g)
    return 0
    
    
if __name__ == '__main__':
    pool = mp.Pool()
    m = mp.Manager()
    q = m.Queue()
    for name in range(20):
        q.put(f"msg {name}")
        
        
    # important to add a comma after 'q' input, or it is interpreted as a list of single characters, or wrong in some other way
    for i in range(20):
        pool.apply_async(worker, (q,))

    pool.close()
    pool.join()
    
    