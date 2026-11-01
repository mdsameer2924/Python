import argparse
import sys

"""
in positional_arguments user suppose to give value if he don't give  value then code  throw error to 
support or provide positional_arguments as an option or mandatory here:- we use 

-------------------------------
parse.add_argument("number",nargs="+") here nargs is the attributes which handles these task and value is '+'
-------------------------------
values of nargs attributes
- (None) if we not use then it's require 1 argument not 2 not 0 only 1.
- '*'  if we use this then it's create list our all arguments stores in list it's support 0,1,2,... as much as you want if we don't give arguments it's can create empty list []
- '+' if we use this then requires at least 1 arguments or many all the arguments stores in list
- '?' if we use this then we can give no arugments or max 1 arguments.

"""
parse = argparse.ArgumentParser(
    usage="%(prog)s [option] [number 1] [number 2]",
    description="A Mathematical CLI tool",
)
parse.add_argument("-a", "--add", action="store_true", help="to add number")
parse.add_argument("-s", "--sub", action="store_true", help="to subtract number")
parse.add_argument("-m", "--multi", action="store_true", help="to multiply number")
parse.add_argument(
    "-v", "--version", action="store_true", help="to check latest version"
)
parse.add_argument(
    "num1", type=float, nargs="+", help="number 1 to perform calculation."
)
# parse.add_argument("num2", type=float, nargs=2, help="number 2 to perfrom calculation")
get_parse = parse.parse_args()
print(get_parse.num1)
try:
    if get_parse.sub:
        print(get_parse.num1[0] - get_parse.num1[1])

    if get_parse.add:
        print(get_parse.num1[0] + get_parse.num1[1])

    if get_parse.multi:
        print(get_parse.num1[0] * get_parse.num1[1])

    if get_parse.version:
        print("sameer's app latest version: 34:35")
except TypeError:
    print("provide number while using math util flag")
    print(f"for example: {sys.argv[0]} -s 4 9 ")
    sys.exit(1)
