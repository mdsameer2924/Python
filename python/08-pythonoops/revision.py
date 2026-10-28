"""
__init__ constructor: Accept owner (string) and initialize a private attribute __balance starting at 0.

Getter method: Create a method named get_balance() that returns the current balance.

Deposit method: Create a method named deposit(amount) that adds money to __balance only if the amount is greater than zero. If it's zero or negative, print a warning message.

Withdraw method: Create a method named withdraw(amount) that subtracts money only if the amount is greater than zero and you have enough funds in __balance.
If not, print an error message (insufficient funds or invalid amount).

Test your code by:

Creating an account for "Sameer".

Depositing 5000.

Trying to withdraw 6000 (should fail safely).

Withdrawing 2000 (should succeed).

Printing the final balance using your getter.

Drop your code for this first problem whenever you're ready


"""
