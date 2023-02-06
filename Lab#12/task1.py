from multiprocessing import Process, Value

def update_value(val,i):
    val.value += 1
    print(f"Value after child process {i}:", val.value)

if __name__ == '__main__':
    shared_value = Value('i', 0)
    print("Value before child processes:", shared_value.value)
    processes = []
    for i in range(5):
        p = Process(target=update_value, args=(shared_value,i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print("Value after all child processes:", shared_value.value)




