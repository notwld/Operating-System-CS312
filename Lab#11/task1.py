from multiprocessing import Process, Pipe
import sys

def f(conn):
    name = conn.recv()
    print(f"Hi {name}, Your roll no is 20b-115-se")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    name = sys.argv[1]
    p = Process(target=f, args=(child_conn,))
    p.start()
    parent_conn.send(name)
    p.join()