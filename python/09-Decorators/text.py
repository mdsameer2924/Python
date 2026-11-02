import subprocess
import sys


def generate_password(func):
    def wrapper(*args, **kwargs):
        try:
            # 1. Converted integer 18 to string str(18) for subprocess
            with open(newp, "w") as file_create:
                subprocess.run(
                    [pass_script, str(18)],
                    check=True,
                    stdout=file_create,
                    stderr=subprocess.DEVNULL,
                )
                log.log_ok("Password generated in pass")

        except subprocess.CalledProcessError:
            log.log_err("Check source code, something went wrong")
            sys.exit(1)
        except OSError:
            log.log_err("Unexpected error: different OS than expected")
            sys.exit(1)

        # 2. Accept and pass arguments, and return the function's result
        return func(*args, **kwargs)

    return wrapper
