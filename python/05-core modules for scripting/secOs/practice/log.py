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
