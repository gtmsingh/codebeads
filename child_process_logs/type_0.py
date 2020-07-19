from utils import run_process

if __name__ == "__main__":
    proc = run_process()

    if proc.poll() is None:
        for line in proc.stdout:
            print(f"STDOUT from process: {line.decode('utf-8').strip()}")
    
    print("Waiting for process to complete")
    proc.wait()
    if proc.poll() > 0:
        if proc.stderr:
            for line in proc.stderr:
                print(f"STDERR from process: {line.decode('utf-8').strip()}")
    
    print("Done!")