# perform multiproc on an array of shared type
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double
from numba.typed import Dict
from numba.types import int64


class Point(Structure):
    _fields_ = [('node_id', c_double), ('node_value', c_double)]


def modify(A):
    for i in range(len(A)):
        A[i] = A[i] + 10
        
def process_structure(A):
    for a in A:
        print(a.node_id)

if __name__ == '__main__':
    
    print('start')
    lock = Lock()
    
    A = Array(c_double, [1.875,-6.25, 9.5], lock=lock)
    print(A)
    
            
    for i in range(3):
        p = Process(target=modify, args=(A,))
        p.start()
        
    for i in range(3):
        p.join()

    for a in A:
        print(a)
        
    # another process for our new Point structure  
    struct_array = Array(Point, [(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock=lock)
    p = Process(target=process_structure, args=(struct_array,))
    p.start()
    p.join()
    
    
    
    
    
    
    
    
    
    
    
    
    