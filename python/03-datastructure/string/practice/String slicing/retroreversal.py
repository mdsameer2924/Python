"""
Challenge #2: "The Retro Reversal"
You are given a string where several words have been written completely backward:

Python
data = "98765_sgnirts_nohtyP_fo_retsam_eht_era_uoY"
Your Goal
Write a single line of Python code using only string slicing (concatenation + and slicing [start:stop:step])
to transform data into the clean, readable sentence:
YOU ARE THE MASTER OF PYTHON STRINGS
"""

data = "98765_sgnirts_nohtyP_fo_retsam_eht_era_uoY"

word = (
    data[-1:-4:-1].upper()
    + " "
    + data[-5:-8:-1].upper()
    + " "
    + data[-9:-12:-1].upper()
    + " "
    + data[-13:-19:-1].upper()
    + " "
    + data[-20:-22:-1].upper()
    + " "
    + data[-23:-29:-1].upper()
    + " "
    + data[-30:-37:-1].upper()
)
print(word)
