import threading
from time import sleep
from utils import run_process


def handle_logs(proc):
    for line in proc.stdout:
        print(f"STDOUT from process: {line.decode('utf-8').strip()}")

    if proc.stderr:
        for line in proc.stderr:
            print(f"STDERR from process {line.decode('utf-8').strip()}")


def run():
    proc = thread = None
    try:
        # Run the script as another process
        proc = run_process()

        # Pass the process handler to the thread for handling stdout and stderr
        thread = threading.Thread(target=handle_logs, args=(proc, ))
        thread.start()

        # Do whatever you want in the mean time
        for i in range(10):
            print("<<<<<<<<<<<<<<< Doing something else >>>>>>>>>>>>>>>")
            sleep(2)
    finally:
        # Wait for the process to complete
        if proc:
            print("Waiting for the process to complete")
            retcode = proc.wait()
            print(f"Process exited with exit code: {retcode}")

        # Wait for the thread to complete
        if thread:
            print("Waiting for the thread to exit")
            thread.join()

    print("Done!")


if __name__ == "__main__":
    run()
