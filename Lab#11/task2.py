from multiprocessing import Process, Pipe

def child_process(conn):
    for i in range(1, 5):
        conn.send(i**2)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    for i in range(1, 5):
        print(parent_conn.recv())
    p.join()