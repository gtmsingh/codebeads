import subprocess
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

def run_process():
    print("Started execution")
    print(sys.platform)
    if sys.platform in ["linux", 'darwin', 'cygwin']:
        print("Running shell script")
        proc = subprocess.Popen(f"sh {CURRENT_DIR}/process.sh", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
    else:
        print("Running batch script")
        proc = subprocess.Popen(f"{CURRENT_DIR}\process.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    # Check if process has started properly
    if proc.poll() not in [None, 0]:
        print(f"Process didn't execute properly (Exit code: {proc.returncode}): {proc.stdout.read()} | {proc.stderr.read()}")
        sys.exit(1)

    return proc
