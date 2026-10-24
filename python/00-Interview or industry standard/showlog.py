"""
This is module which follow dry principal which mean do not repeat yourself
Where use Industry practice to dispaly status of code

"""

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def log_err(msg):
    print(f"{RED}[FAIL]{RESET} {msg}")


def log_ok(msg):
    print(f"{GREEN}[ OK ]{RESET} {msg}")


def log_warn(signal):
    print(f"{YELLOW}[WARN]{RESET} {signal}")


def log_info(msg):
    print(f"{CYAN}[ .. ]{RESET} {msg}")
