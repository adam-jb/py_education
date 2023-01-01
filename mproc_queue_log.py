import multiprocessing as mp
import logging
import os
import time

def logger_process(queue): 
    # setup
    logfilepath=filename=os.getcwd()+'/example.log'
    logging.basicConfig(filename=logfilepath, encoding='utf-8', level=logging.DEBUG)
    print('logger worker ready')
    
    # Loop indefinitely
    while True:
        # Get the next item from the queue
        msg = queue.get()
        print(f'msg: {msg}')
        
        if msg == 'CLOSE':
            break
        else:
            print(f'logging: {msg}')
            logging.info(msg)
     
def task_process(queue, logging_queue): 

    # Loop indefinitely
    while True:
        # Get the next item from the queue
        msg = queue.get()
        if msg == 'CLOSE':
            break
        else:
            print(f'do something with msg {msg}')
            logging_queue.put(f'msg log of {msg}')

def main():
    # Create queues
    logging_queue = mp.Queue()
    tasks_queue = mp.Queue()

    # Create a logger process
    logger_worker_process = mp.Process(target=logger_process, args=(logging_queue,))
    logger_worker_process.start()

    # Create process for main tasks
    task_worker_process = mp.Process(target=task_process, args=(tasks_queue,logging_queue, ))
    task_worker_process.start()

    # send some tasks to main tasks
    # Put some items in the queue
    tasks_queue.put("item 1")
    tasks_queue.put("item 2")
    tasks_queue.put("item 3")

    tasks_queue.put("CLOSE")
    time.sleep(1)
    logging_queue.put("CLOSE")


if __name__ == "__main__":
    main()

# cleanup
"""
task_worker_process.join()
logger_worker_process.join()
"""





