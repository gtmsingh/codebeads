import subprocess
import sys
import threading
from time import sleep
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

def handle_logs(proc: subprocess.Popen):
    for line in proc.stdout:
        print(f"STDOUT from process: {line.decode('utf-8')}")

    if proc.stderr:
        for line in proc.stderr:
            print(f"STDERR from process {line.decode('utf-8')}")

def run_process():
    print("Started execution")
    print(sys.platform)
    if sys.platform in ["linux", 'darwin', 'cygwin']:
        print("Running shell script")
        proc = subprocess.Popen(f"sh {CURRENT_DIR}/process.sh", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
        print("Running batch script")
        proc = subprocess.Popen(f"{CURRENT_DIR}\process.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    return proc



def run():
    proc = thread = None
    try:
        # Run the script as another process
        proc = run_process()

        # Check if process has started properly
        if proc.poll() not in [None, 0]:
            print(f"Process didn't execute properly (Exit code: {proc.returncode}): {proc.stdout.read()} | {proc.stderr.read()}")
        
        # Pass the process handler to the thread for handling stdout and stderr
        thread = threading.Thread(target=handle_logs, args=(proc, ))
        thread.start()
        
        # Do whatever you want in the mean time
        for i in range(10):
            print("Doing something else")
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