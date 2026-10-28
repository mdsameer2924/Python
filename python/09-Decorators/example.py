import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        # --- COMPLEX LOGIC BEFORE ---
        print(f"--> Starting execution of '{func.__name__}'...")
        start_time = time.time()

        # Run the actual function (and catch its return value)
        result = func(*args, **kwargs)

        # --- COMPLEX LOGIC AFTER ---
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"<-- Finished '{func.__name__}' in {elapsed:.6f} seconds\n")

        return result  # Don't forget to return the result!

    return wrapper


@measure_time
def add(a: int, b: int) -> int:
    # Simulate a heavy calculation
    time.sleep(1)
    return a + b


@measure_time
def greet(name: str):
    print(f"Hello, {name}!")


# Testing them out:
sum_result = add(5, 10)
print(f"Result: {sum_result}\n")

greet("Sameer")


def sbi():
    print(sbi.__name__)


sbi()
