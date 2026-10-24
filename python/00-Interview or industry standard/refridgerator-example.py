import showlog as show


def check_fridge_status(is_on, temperature):
    # Buggy check!
    if is_on and temperature is not None:
        show.log_ok(f"Fridge is running normally at {temperature}°C.")
    else:
        show.log_warn(": Fridge is OFF or temperature is unreadable!")


# Testing when temperature is 0°C
check_fridge_status(is_on=True, temperature=None)
