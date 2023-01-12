import queue
from logging.handlers import QueueHandler

log_queue     = queue.Queue()
queue_handler = QueueHandler(log_queue)  # Non-blocking handler.

root = logging.getLogger()
root.addHandler(queue_handler) 



from logging.handlers import QueueListener
from logging.handlers import RotatingFileHandler

rot_handler    = RotatingFileHandler(...)   # The blocking handler.
queue_listener = QueueListener(log_queue, 
                               rot_handler) # Sitting comfortably in its
                                            # own thread, isolated from
                                            # async code.
queue_listener.start()
