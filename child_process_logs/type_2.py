from utils import run_process
from queue import Queue, Empty
from threading import Thread
from time import sleep

# Referenced from: https://stackoverflow.com/a/4896288/3970917

def enqueue_output(out, queue):
    for line in out:
        queue.put(line)

def run():
    proc = run_process()
    q = Queue()
    thread = Thread(target=enqueue_output, args=(proc.stdout, q))
    thread.start()
    # I don't need this thread as stderr is being streamed to stdout
    # thread2 = Thread(target=enqueue_error, args=(proc.stderr, q))
    # thread2.start()

    while proc.poll() is None or not q.empty():
        # read line without blocking
        # You can have timeout also
        while not q.empty():
            line = q.get_nowait() # or q.get(timeout=.1)
            print(f"STDOUT from process: {line.decode('utf-8')}")

        sleep(3)
        # Do something else
        print("<<<<<<<<<<<<<<< Doing something else >>>>>>>>>>>>>>>")
    
    print("Waiting for the thread to complete")
    thread.join()

    print("Waiting for process to complete")
    proc.wait()



if __name__ == "__main__":
    run()