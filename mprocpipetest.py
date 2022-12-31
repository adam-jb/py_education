# in the case of Pipe(), everything happens wherever we call parent_conn.recv()
# whereas if using Process() alone it happens on p.join()
from multiprocessing import Process, Pipe

def f(conn, intval):
    conn.send([intval, None, 'hello'])
    conn.close()
    print(intval)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    procs = []
    for i in range(3):
        p = Process(target=f, args=(child_conn,i,))
        procs.append(p)
        p.start()
        #print(parent_conn.recv())   # prints "[42, None, 'hello']"
    print('done')
    for p in procs:
        print(parent_conn.recv())
        p.join()
    