## ERROR Logger
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def log_err(msg):
    print(f"{RED}[FAIL]{RESET} {msg}")


def log_ok(msg):
    print(f"{GREEN}[ OK ]{RESET} {msg}")


def log_info(msg):
    print(f"{CYAN}[ .. ]{RESET} {msg}")


def log_warn(msg):
    print(f"{YELLOW}[WARN]{RESET} {msg}")

    # if __name__ == "__main__":
    log_err("This is for error or any failed operations")
    log_info("This is for any information")
    log_warn("Any kind of warning")
