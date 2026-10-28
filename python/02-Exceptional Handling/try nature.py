try:
    print("Step 1: This runs successfully")
    # 1 / 0  # If you uncomment this, Step 2 is skipped completely!
    print("Step 2: This runs only if Step 1 succeeds")
except ZeroDivisionError:
    print("Caught an error!")
