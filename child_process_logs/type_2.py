from utils import run_process
from queue import Queue, Empty
from threading import Thread
from time import sleep

# Referenced from: https://stackoverflow.com/a/4896288/3970917


def enqueue_logs(process, queue):
    for line in process.stdout:
        queue.put(line)


def handle_logs(proc, queue):
    while proc.poll() is None or not queue.empty():
        # read line without blocking
        # You can have timeout also
        if queue.empty():
            sleep(0.5)
            continue

        line = queue.get_nowait()  # or q.get(timeout=.1)
        print(f"STDOUT from process: {line.decode('utf-8').strip()}")


def run():
    proc = run_process()
    q = Queue()
    thread = Thread(target=enqueue_logs, args=(proc, q))
    thread.start()

    thread2 = Thread(target=handle_logs, args=(proc, q))
    thread2.start()
    for i in range(5):
        # Do something else
        print("<<<<<<<<<<<<<<< Doing something else >>>>>>>>>>>>>>>")
        sleep(1)

    print("Waiting for the thread to complete")
    thread.join()
    thread2.join()

    print("Waiting for process to complete")
    proc.wait()


if __name__ == "__main__":
    run()
