from re import sub
import subprocess
import time

try:
    s = subprocess.run(
        [
            "sleep",
            "2",
        ],
        shell=False,
        timeout=6,
        check=True,
    )
    subprocess.run(["echo", "Hello world"])

except subprocess.TimeoutExpired:
    time.sleep(1)
    print("Time pura hua haaha")
except subprocess.CalledProcessError:
    time.sleep(1.19)
    print("check error aa gaya")
finally:
    print("code execute sucessuflly")
